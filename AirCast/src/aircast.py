from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('src/model.pkl')  # Adjust if needed

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Dummy logic
    return "Prediction logic here"

if __name__ == '__main__':
    app.run(debug=True)
