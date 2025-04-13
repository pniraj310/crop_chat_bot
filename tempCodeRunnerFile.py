import streamlit as st
import uuid  # Import uuid to generate GUID
from model import predict_yield
from crop_info import crop_details, state_based_crops, state_season_crop_map, crop_yield_ranges
import os

# Set page config first
st.set_page_config(page_title="\U0001F33E AI Crop Yield Chatbot", page_icon="\U0001F33E", layout="wide")

# Apply custom CSS for layout
st.markdown("""
    <style>
        .title-section {
            background-color: #4CAF50;
            color: white;
            padding: 40px 10px 10px;
            text-align: center;
        }
        .main-section {
            background-color: #fdfdfd;
            padding: 20px;
        }
        .footer-section {
            background-color: #1c1c1c;
            color: white;
            padding: 15px 20px;
        }
        .footer-link {
            color: #ccc;
            text-decoration: none;
        }
        .footer-link:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE SECTION ----------
st.markdown('<div class="title-section"><h1>\U0001F33E AI Crop Yield Chatbot</h1><p>Empowering Indian Farmers With Smart Predictions</p></div>', unsafe_allow_html=True)

# ---------- MAIN SECTION ----------
st.markdown('<div class="main-section">', unsafe_allow_html=True)

# Generate a GUID for the current session
if "guid" not in st.session_state:
    st.session_state.guid = str(uuid.uuid4())  # Generate GUID if not already present

st.write(f"Your session GUID: {st.session_state.guid}")

st.subheader("\U0001F4CD Select Region & Season")
state = st.selectbox("Select your state:", list(state_season_crop_map.keys()))
season = st.selectbox("Select the season:", ["Kharif", "Rabi", "Zaid", "Cash Crops"])

if state in state_season_crop_map and season in state_season_crop_map[state]:
    crops_in_season = state_season_crop_map[state][season]
    if crops_in_season:
        st.success(f"Crops grown in {state} during {season} season: {', '.join(crops_in_season)}")
    else:
        st.warning("No crops listed for this state and season.")

st.subheader("\U0001F50D Predict Crop Yield")

crop = st.selectbox("Select your crop:", list(crop_details.keys()))
temperature = st.slider("\U0001F321️ Average temperature (°C):", 10, 45, 25)
rainfall = st.slider("\U0001F327️ Expected rainfall (mm):", 0, 300, 100)

# Show crop image
image_extensions = ["jpg", "jpeg", "png"]
image_found = False
for ext in image_extensions:
    image_path = f"crop_images/{crop.lower()}.{ext}"
    if os.path.exists(image_path):
        st.image(image_path, caption=f"{crop}", width=300)
        image_found = True
        break
if not image_found:
    st.info("Image not available for this crop.")

if crop in crop_details:
    st.markdown(f"**\U0001F4C5 Season of {crop}:** {crop_details[crop]['season']}")
    st.markdown(f"**\U0001F4CD Commonly grown in:** {crop_details[crop]['states']}")

if st.button("\U0001F4CA Predict Yield"):
    result = predict_yield(crop, temperature, rainfall)

    if crop in crop_yield_ranges:
        ranges = crop_yield_ranges[crop]
        if result >= ranges["good"]:
            level = "\U0001F7E2 Good Yield"
        elif result >= ranges["average"]:
            level = "\U0001F7E1 Average Yield"
        else:
            level = "\U0001F534 Poor Yield"
        st.success(f"\u2705 Estimated Yield for {crop}: **{result} tons/acre**")
        st.info(f"\U0001F33E Yield Level: **{level}**")
    else:
        st.success(f"\u2705 Estimated Yield for {crop}: **{result} tons/acre**")
        st.warning("\u26A0\uFE0F Yield category not available for this crop.")

# ---------- Chatbot Section ----------
st.markdown("### \U0001F4AC Ask Anything About Agriculture")

# Initialize chat history if not already in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input from user
user_input = st.text_input("\U0001F9D1 You:", placeholder="Ask me about crops, seasons, soil, etc...")

# Process user input and generate bot response
if user_input:
    def get_bot_response(user_msg):
        user_msg = user_msg.lower()
        if "best crop" in user_msg or "which crop" in user_msg:
            return f"In {state}, during {season}, you can grow: {', '.join(state_season_crop_map[state][season])}"
        elif "rainfall" in user_msg:
            return "Most Kharif crops need good rainfall, around 100-200mm is ideal."
        elif "temperature" in user_msg:
            return "Rabi crops prefer cooler temperatures (10-25°C), while Kharif crops prefer warmer (25-35°C)."
        elif "soil" in user_msg:
            return "Black soil is good for cotton, alluvial for rice and wheat, loamy for vegetables."
        else:
            return "I'm still learning! Try asking about crops, seasons, soil, rainfall, or temperature."

    # Get the bot's reply
    bot_reply = get_bot_response(user_input)

    # Store user and bot messages in session state
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "bot", "content": bot_reply})

# Display the chat history using Streamlit's st.chat_message
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**You**: {msg['content']}")
    else:
        st.markdown(f"**Bot**: {msg['content']}")

# ---------- FOOTER SECTION ----------
st.markdown('<div class="footer-section">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("#### ℹ️ About Us", unsafe_allow_html=True)
    st.markdown("<small>We are a student team aiming to help farmers using AI for crop yield prediction.</small>", unsafe_allow_html=True)
    st.markdown("#### 📧 Help", unsafe_allow_html=True)
    st.markdown("<small>Email: pniraj310@gmail.com</small>", unsafe_allow_html=True)
    st.markdown("<small>WhatsApp: 9309826762</small>", unsafe_allow_html=True)
    st.markdown("#### 🏫 College", unsafe_allow_html=True)
    st.markdown("<small>G. V. Acharya Institute Of Engineering and Technology, Shelu</small>", unsafe_allow_html=True)

with col2:
    st.markdown("#### 📜 Policies", unsafe_allow_html=True)
    st.markdown('<small><a class="footer-link" href="#">Privacy Policy</a> | <a class="footer-link" href="#">Terms</a> | <a class="footer-link" href="#">Support</a></small>', unsafe_allow_html=True)

# Add GUID for Suraj Chopde here
st.markdown('<div style="text-align: center; font-size: 12px; color: #ccc;">', unsafe_allow_html=True)
st.markdown("<p>GUID: Suraj Chopde (Edunet Trainer) </p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr style="border-color:#666;">', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; font-size: 12px; color: #ccc;">
        <p>© 2025 AI Crop Yield Bot | Made with ❤️ by Dhruv Gupta and Team</p>
        <p>Group Leader: Dhruv Gupta | Members: Niraj, Ritesh, Atharva, Aditya</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
