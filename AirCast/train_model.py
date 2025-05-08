import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample dummy data: [PM2.5, PM10, Temp, Humidity]
X = np.array([
    [35, 60, 25, 55],
    [90, 120, 30, 60],
    [15, 30, 20, 50],
    [55, 80, 28, 70]
])

# Corresponding AQI values (dummy)
y = np.array([100, 200, 50, 150])

# Train a simple model
model = LinearRegression()
model.fit(X, y)

# Save the model inside the src directory
joblib.dump(model, 'src/model.pkl')

print("✅ Model trained and saved as src/model.pkl")
