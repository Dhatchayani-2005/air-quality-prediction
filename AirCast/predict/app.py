from flask import Flask, render_template, request
import os
print("Files in templates folder:", os.listdir("templates"))


app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    pm25 = float(request.form['pm25'])
    pm10 = float(request.form['pm10'])
    temp = float(request.form['temp'])
    humidity = float(request.form['humidity'])

    # Dummy prediction logic (replace with model)
    aqi = (pm25 + pm10 + temp + humidity) / 4

    return render_template('index.html', prediction=round(aqi, 2))

if __name__ == '__main__':
    app.run(debug=True)
