import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import time
from playsound import playsound

# Load the trained model
model = RandomForestClassifier()  # Replace with your trained model

# Load the CSV data
data = pd.read_csv("earthquake_data.csv")

# Extract features and labels
X = data.drop("label", axis=1).values
y = data["label"].values

# Simulate real-time earthquake detection
while True:
    new_data = np.random.rand(1, 10)  # Replace with actual data acquisition
    
    # Predict using the loaded model
    prediction = model.predict(new_data)
    
    if prediction == 1:
        print("Earthquake detected! Playing alarm sound...")
        playsound("alarm_sound.mp3")  # Replace with the path to your alarm sound file
    else:
        print("No earthquake detected.")
    
    time.sleep(5)  # Simulate waiting time before next prediction
