import base64
import streamlit as st
from model import predict_yield
from crop_info import crop_details, state_based_crops, state_season_crop_map
from streamlit_chat import message
from crop_info import crop_yield_ranges

# Set page configuration as the first command
st.set_page_config(page_title="AI Crop Yield Chatbot", page_icon="🌾")

# Function to add background image from a local file
def add_bg_from_local(image_path, section=""):
    # Load the image from the file
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    
    # Apply background image with specific section (title, main, or contact)
    if section == "title":
        st.markdown(
            f"""
            <style>
            .title-section {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 400px;
                text-align: center;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    elif section == "main":
        st.markdown(
            f"""
            <style>
            .main-section {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                min-height: 500px;
                padding: 40px;
                color: white;
                text-align: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    elif section == "contact":
        st.markdown(
            f"""
            <style>
            .contact-section {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                padding: 40px;
                color: white;
                text-align: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Path to your local images
title_bg_path = "E:/crop_chat_bot/images/title_bg.jpg"  # Title background image path
main_bg_path = "E:/crop_chat_bot/images/bg image.jpg"    # Main section background image path
contact_bg_path = "E:/crop_chat_bot/images/contact_section.jpg"  # Contact section background image path

# Add background image for the title section
add_bg_from_local(title_bg_path, section="title")

# --- Title Section ---
st.markdown("<div class='title-section'>", unsafe_allow_html=True)
st.title("🌾 Sustainable Agriculture Chatbot")
st.markdown("Get crop yield predictions and know what crops grow best in your region and season.")
st.markdown("</div>", unsafe_allow_html=True)

# Add background image for the main section
add_bg_from_local(main_bg_path, section="main")

# --- Main Section ---
st.markdown("<div class='main-section'>", unsafe_allow_html=True)
# --- State and Season Selection ---
state = st.selectbox("🌍 Select your state:", list(state_season_crop_map.keys()))
season = st.selectbox("🗓️ Select the season:", ["Kharif", "Rabi", "Zaid", "Cash Crops"])

# --- Show Recommended Crops for Selected State and Season ---
if state in state_season_crop_map and season in state_season_crop_map[state]:
    crops_in_season = state_season_crop_map[state][season]
    if crops_in_season:
        st.markdown(f"**🌱 Crops grown in {state} during {season} season:** {', '.join(crops_in_season)}")
    else:
        st.warning(f"No crops listed for {state} in {season} season.")

# --- Yield Prediction Section ---
st.subheader("🔍 Predict Crop Yield")

crop = st.selectbox("🌾 Select your crop:", list(crop_details.keys()))
temperature = st.slider("🌡️ Enter average temperature (°C):", 10, 45, 25)
rainfall = st.slider("🌧️ Enter expected rainfall (mm):", 0, 300, 100)

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

# --- Season-wise Crops in Your State ---
st.markdown("### 🧭 Season-wise Crops in Your State:")
for s, crops in state_season_crop_map[state].items():
    if crops:
        st.markdown(f"**{s} Season:** {', '.join(crops)}")
    else:
        st.markdown(f"**{s} Season:** No data available.")

# --- Chatbot Section ---
st.markdown("---")
st.subheader("💬 Ask Anything About Agriculture")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("🧑 You:", placeholder="Ask me about crops, seasons, soil, etc...")

if user_input:
    # Sample hardcoded responses (you can improve this with NLP or ChatGPT API later)
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

st.markdown("</div>", unsafe_allow_html=True)

# Add background image for the contact section
add_bg_from_local(contact_bg_path, section="contact")

# --- Footer Section (Contact, About, Privacy Policy, Help) ---
st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
st.markdown("### 📝 Contact Information")
st.markdown("For any inquiries, please email us at: **contact@cropyield.com**")

st.markdown("### 📚 About Us")
st.markdown("We are a group of students from GV Acharya Institute of Engineering and Technology, working on AI-based agriculture solutions to support sustainable farming.")

st.markdown("### 🔒 Privacy Policy")
st.markdown("We respect your privacy and ensure that all personal data is handled securely and only for the purpose of providing services.")

st.markdown("### ❓ Help")
st.markdown("If you need help, please reach out to us at our contact section above or email us directly.")
st.markdown("</div>", unsafe_allow_html=True)
