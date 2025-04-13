import streamlit as st
from model import predict_yield
from crop_info import crop_details, state_based_crops, state_season_crop_map, crop_yield_ranges
from streamlit_chat import message
import os

# Set page config first
st.set_page_config(page_title="🌾 AI Crop Yield Chatbot", page_icon="🌾", layout="wide")

# Apply custom CSS for layout
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .title-section {
            background-color: #4CAF50;  # Keeping the same green for the title section
            color: white;
            padding: 40px 10px 10px;
            text-align: center;
        }
        .main-section {
            background-color: #ffffff;  # Light white background for main section
            padding: 20px;
            border-radius: 10px;  # Rounded corners for better appearance
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  # Subtle shadow for depth
        }
        .contact-section {
            background-color: #232F3E;  # Dark blue for the contact section
            color: white;
            padding: 30px 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  # Adding depth with shadow
        }
        .footer-link {
            color: #ddd;
            margin-right: 15px;
            text-decoration: none;
        }
        .footer-link:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE SECTION ----------
st.markdown('<div class="title-section"><h1>🌾 AI Crop Yield Chatbot</h1><p>Empowering Indian Farmers With Smart Predictions</p></div>', unsafe_allow_html=True)

# ---------- MAIN SECTION ----------
st.markdown('<div class="main-section">', unsafe_allow_html=True)

st.subheader("📍 Select Region & Season")
state = st.selectbox("Select your state:", list(state_season_crop_map.keys()))
season = st.selectbox("Select the season:", ["Kharif", "Rabi", "Zaid", "Cash Crops"])

if state in state_season_crop_map and season in state_season_crop_map[state]:
    crops_in_season = state_season_crop_map[state][season]
    if crops_in_season:
        st.success(f"Crops grown in {state} during {season} season: {', '.join(crops_in_season)}")
    else:
        st.warning("No crops listed for this state and season.")

st.subheader("🔍 Predict Crop Yield")

crop = st.selectbox("Select your crop:", list(crop_details.keys()))
temperature = st.slider("🌡️ Average temperature (°C):", 10, 45, 25)
rainfall = st.slider("🌧️ Expected rainfall (mm):", 0, 300, 100)

# Show crop image
image_path = f"crop_images/{crop.lower()}.jpg"
if os.path.exists(image_path):
    st.image(image_path, caption=f"{crop}", width=300)
else:
    st.info("Image not available for this crop.")

if crop in crop_details:
    st.markdown(f"**🗓️ Season of {crop}:** {crop_details[crop]['season']}")
    st.markdown(f"**📍 Commonly grown in:** {crop_details[crop]['states']}")

if st.button("📊 Predict Yield"):
    result = predict_yield(crop, temperature, rainfall)

    if crop in crop_yield_ranges:
        ranges = crop_yield_ranges[crop]
        if result >= ranges["good"]:
            level = "🟢 Good Yield"
        elif result >= ranges["average"]:
            level = "🟡 Average Yield"
        else:
            level = "🔴 Poor Yield"
        st.success(f"✅ Estimated Yield for {crop}: **{result} tons/acre**")
        st.info(f"🌾 Yield Level: **{level}**")
    else:
        st.success(f"✅ Estimated Yield for {crop}: **{result} tons/acre**")
        st.warning("⚠️ Yield category not available for this crop.")

# --- Chatbot Section ---
st.markdown("### 💬 Ask Anything About Agriculture")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("🧑 You:", placeholder="Ask me about crops, seasons, soil, etc...")

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

    bot_reply = get_bot_response(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "bot", "content": bot_reply})

# Display chat history
for msg in st.session_state.chat_history:
    message(msg["content"], is_user=(msg["role"] == "user"))

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer with Team Info ----------
st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #2c3e50; color: white; border-radius: 10px;">
        <h4>Team Information:</h4>
        <p><strong>Group Leader:</strong> Dhruv Gupta</p>
        <p><strong>Members:</strong> Niraj Patel, Ritesh Dalal, Atharva Ghodke, Aditya Ankashkar</p>
        <p><strong>College:</strong> GV Acharya Institute of Engineering and Technology (GVAIET)</p>
        <p><strong>Project Title:</strong> Sustainable Agriculture with AI for Crop Yield Prediction</p>
        <p><strong>Contact:</strong> 📞 9309826762 | 📧 pniraj310@gmail.com</p>
        <p><strong>Under the guidance of:</strong> Suraj Chopde (Edunet Trainer)</p>
        <hr style="border-color:#444;">
        <h5>About Us</h5>
        <p>We are a student team aiming to help farmers using AI for crop yield prediction.</p>
        <h5>Help</h5>
        <p>Email us at: <a href="mailto:support@cropai.in" style="color: #ddd;">support@cropai.in</a></p>
        <h5>Policies</h5>
        <p><a href="#" class="footer-link" style="color: #ddd;">Privacy Policy</a></p>
        <p><a href="#" class="footer-link" style="color: #ddd;">Terms of Use</a></p>
        <p><a href="#" class="footer-link" style="color: #ddd;">Support</a></p>
    </div>
""", unsafe_allow_html=True)
