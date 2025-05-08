# AirCast – Air Quality Prediction System

AirCast is an AI-based system that predicts Air Quality Index (AQI) based on environmental data (e.g., PM2.5, PM10, temperature, humidity). It uses a simple ML model with a Flask-based web interface for live predictions.

## Features
- AQI prediction using regression
- Flask web app for real-time input & output
- Extendable with real-time sensors or APIs

## Structure
- `src/`: ML code and main logic
- `data/`: Sample air quality datasets
- `models/`: Saved model files
- `templates/` & `static/`: Flask front-end

## To Run
```bash
pip install -r requirements.txt
python src/aircast.py
