import streamlit as st
from model import predict_yield
from crop_info import crop_details, state_based_crops, state_season_crop_map
from crop_info import crop_yield_ranges

# Set page configuration at the top
st.set_page_config(page_title="AI Crop Yield Chatbot", page_icon="🌾")

# Hide Streamlit's default UI elements (menu, footer, header)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {
        background-color: #f4f7fa;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 30px;
        color: #2c3e50;
        text-align: center;
        margin-top: 50px;
    }
    .subheader {
        font-size: 25px;
        color: #3498db;
        text-align: center;
    }
    .button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        cursor: pointer;
        border-radius: 5px;
        font-size: 18px;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #2980b9;
    }
    .crop-info {
        margin-top: 30px;
        padding: 10px;
        border-radius: 5px;
        background-color: #ecf0f1;
    }
    .chat-history {
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        margin-top: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Custom JavaScript for additional interaction (like opening a popup on clicking a button)
st.markdown("""
    <script>
    function showAlert() {
        alert("Welcome to the AI Crop Yield Chatbot!");
    }
    </script>
""", unsafe_allow_html=True)

# Set up page title
st.markdown('<div class="title">🌾 Sustainable Agriculture Chatbot</div>', unsafe_allow_html=True)
st.markdown("Get crop yield predictions and know what crops grow best in your region and season.")

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
st.markdown('<div class="subheader">🔍 Predict Crop Yield</div>', unsafe_allow_html=True)

crop = st.selectbox("🌾 Select your crop:", list(crop_details.keys()))
temperature = st.slider("🌡️ Enter average temperature (°C):", 10, 45, 25)
rainfall = st.slider("🌧️ Enter expected rainfall (mm):", 0, 300, 100)

if crop in crop_details:
    st.markdown(f"**🗓️ Season of {crop}:** {crop_details[crop]['season']}")
    st.markdown(f"**📍 Commonly grown in:** {crop_details[crop]['states']}")

if st.button("📊 Predict Yield", key="predict_button"):
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

    st.markdown("### 🧭 Season-wise Crops in Your State:")
    for s, crops in state_season_crop_map[state].items():
        if crops:
            st.markdown(f"**{s} Season:** {', '.join(crops)}")
        else:
            st.markdown(f"**{s} Season:** No data available.")

# --- Chatbot Section ---
st.markdown("<div class='subheader'>💬 Ask Anything About Agriculture</div>", unsafe_allow_html=True)

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
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

# --- Display Chat History with Scrollable Area ---
st.markdown('<div class="chat-history">', unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.write(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

# Add button to show alert with JS interaction (for testing JavaScript)
st.button("Show Welcome Alert", on_click=lambda: st.markdown("<script>showAlert()</script>", unsafe_allow_html=True))
