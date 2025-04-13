import streamlit as st
from model import predict_yield
from crop_info import crop_details, state_based_crops, state_season_crop_map
from crop_info import crop_yield_ranges

st.set_page_config(page_title="AI Crop Yield Chatbot", page_icon="🌾")

st.title("🌾 Sustainable Agriculture Chatbot")
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

    st.markdown("### 🧭 Season-wise Crops in Your State:")
    for s, crops in state_season_crop_map[state].items():
        if crops:
            st.markdown(f"**{s} Season:** {', '.join(crops)}")
        else:
            st.markdown(f"**{s} Season:** No data available.")

# --- Chatbot Section ---
st
