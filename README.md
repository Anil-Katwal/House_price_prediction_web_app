# 🏡 Luxury House Price Prediction Web App

Welcome to the **House Price Prediction Web App** — a powerful, intelligent tool that predicts the price of a house based on key features like location, room count, median income, and proximity to the ocean.

This project leverages **Machine Learning (ANN - Artificial Neural Network)** and a clean **Streamlit-based web interface** to offer an intuitive, interactive experience for users to estimate real estate prices.

---

## 🚀 Live Demo
<img width="985" alt="Screenshot 2025-06-17 at 2 54 31 PM" src="https://github.com/user-attachments/assets/e6476dcc-62b6-4e25-a9ac-a80795986b28" />


## 📌 Features
🔢 Accurate predictions using a trained ANN regression model

🧠 Keras + TensorFlow backend with Scikit-learn scaling

🌍 Interactive input: latitude, longitude, population, income, and more

🌊 Select ocean proximity via dropdown (e.g., NEAR OCEAN, ISLAND, etc.)

📉 Visual feedback on price estimate

🎯 Deployed using Streamlit for simplicity and performance
## 🧠 Tech Stack

| Technology       | Role                         |
| ---------------- | ---------------------------- |
| Python           | Core programming language    |
| TensorFlow/Keras | Deep learning framework      |
| Scikit-learn     | Data preprocessing (scaling) |
| Streamlit        | Web UI framework             |
| NumPy            | Numerical computation        |
| Pickle           | Model serialization          |
## 🏗️ How It Works
--User inputs data via a clean Streamlit interface

--Inputs are scaled using MinMaxScaler

--The ANN model (model_ann.h5) predicts the price

--The predicted value is displayed dynamically
## 🧪 Model Training Overview
--Trained using California Housing Dataset

--Input features: longitude, latitude, housing age, rooms, bedrooms, income, ocean proximity (encoded)

--Loss: Mean Squared Error (MSE)

--Optimizer: RMSprop

--Evaluation: MAE, R² score
## 📁 Project Structure
House_price_prediction_web_app/

-├── app.py                  # Streamlit frontend
-├── model_ann.h5            # Trained ANN model
-├── scaler.pkl              # Pre-trained MinMaxScaler
-├── requirements.txt        # Python dependencies
-└── README.md               
## 📊 Example Input & Output
| Input Feature   | Value      |
| --------------- | ---------- |
| Latitude        | 37.88      |
| Longitude       | -122.23    |
| House Age       | 25         |
| Rooms           | 1800       |
| Bedrooms        | 400        |
| Population      | 1200       |
| Households      | 350        |
| Median Income   | 4.5        |
| Ocean Proximity | NEAR OCEAN |

## 🙋‍♂️ Author
Anil Katwal
Machine Learning Engineer | Data Scientist
📧 aniljungkatwal@gmail.com
🔗 LinkedIn • GitHub

