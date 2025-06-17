import streamlit as st
from keras.models import load_model
import pickle
import numpy as np

# Load model and scaler
model = load_model("model_ann.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit app
st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏡 Luxuary House Price Prediction")
st.write("Enter the details below to predict the house price:")

# User input fields
longitude = st.number_input("Longitude", value=-122.0, format="%.4f")
latitude = st.number_input("Latitude", value=37.0, format="%.4f")
houseage = st.number_input("House Age (in years)", min_value=0.0, value=20.0)
houserooms = st.number_input("Total Rooms", min_value=1.0, value=1000.0)
totlabedrooms = st.number_input("Total Bedrooms", min_value=1.0, value=200.0)
population = st.number_input("Population", min_value=1.0, value=1000.0)
households = st.number_input("Households", min_value=1.0, value=300.0)
medianincome = st.number_input("Median Income", min_value=0.0, value=3.5)

ocean_dict = {
    "<1H OCEAN": 0,
    "INLAND": 1,
    "NEAR OCEAN": 2,
    "NEAR BAY": 3,
    "ISLAND": 4
}
oceanproximity = st.selectbox("Ocean Proximity", list(ocean_dict.keys()))
ocean_encoded = ocean_dict[oceanproximity]

# Prediction
if st.button("Predict Price"):
    features = np.array([[
        longitude, latitude, houseage, houserooms, totlabedrooms,
        population, households, medianincome, ocean_encoded
    ]], dtype=float)

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0][0]

    st.success(f"🏠 Predicted House Price: **${prediction:,.2f}**")
