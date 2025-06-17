from flask import Flask, request, render_template
from keras.models import load_model
import pickle
import numpy as np

app = Flask(__name__)

# Load the model without compiling to avoid 'mse' error
model = load_model("model_ann.h5", compile=False)
scaler = pickle.load(open('scaler.pkl', 'rb'))
#label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))  # for oceanproximity encoding

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/house", methods=['POST'])
def house():
    if request.method == 'POST':
        try:
            longitude = float(request.form['longitude'])
            latitude = float(request.form['latitude'])
            houseage = float(request.form['houseage'])
            houserooms = float(request.form['houserooms'])
            totlabedrooms = float(request.form['totlabedrooms'])
            population = float(request.form['population'])
            households = float(request.form['households'])
            medianincome = float(request.form['medianincome'])
            oceanproximity = request.form['oceanproximity']

            # Encode categorical feature
            ocean_encoded = label_encoder.transform([oceanproximity])[0]

            features = np.array([longitude, latitude, houseage, houserooms,
                                 totlabedrooms, population, households,
                                 medianincome, ocean_encoded])

            features_scaled = scaler.transform([features])
            price = model.predict(features_scaled)[0][0]
            price = round(price, 2)

            return render_template('index.html', result=f"Predicted House Price: ${price}")
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/doc")
def doc():
    return render_template('doc.html')

if __name__ == "__main__":
    app.run(debug=True)
