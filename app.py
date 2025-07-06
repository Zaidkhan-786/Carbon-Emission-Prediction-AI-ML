import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("forecasting_co2_emmision.pkl")

st.set_page_config(page_title="CO2 Emission Predictor", layout="centered")
st.title("🌿 Carbon Emission Forecasting")
st.write("Predict CO2 emissions based on environmental and economic indicators.")

# Input fields for the 7 features
cereal_yield = st.number_input("🌾 Cereal Yield (kg per hectare)", value=3000.0)
gni_per_cap = st.number_input("💰 GNI per Capita (USD)", value=10000.0)
en_per_cap = st.number_input("⚡ Energy Use per Capita (kg of oil equivalent)", value=2000.0)
pop_urb_aggl_perc = st.number_input("🏙️ Urban Population in Agglomerations (%)", value=60.0)
prot_area_perc = st.number_input("🌱 Protected Area (%)", value=15.0)
pop_growth_perc = st.number_input("👥 Population Growth (%)", value=1.5)
urb_pop_growth_perc = st.number_input("📈 Urban Population Growth (%)", value=2.0)

# Form a dataframe for prediction
input_df = pd.DataFrame([[
    cereal_yield,
    gni_per_cap,
    en_per_cap,
    pop_urb_aggl_perc,
    prot_area_perc,
    pop_growth_perc,
    urb_pop_growth_perc
]], columns=[
    'cereal_yield',
    'gni_per_cap',
    'en_per_cap',
    'pop_urb_aggl_perc',
    'prot_area_perc',
    'pop_growth_perc',
    'urb_pop_growth_perc'
])

# Predict and display result
if st.button("🚀 Predict CO2 Emission"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🌫️ Estimated CO2 Emission: **{prediction:.2f} tons/year**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
