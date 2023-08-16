import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time
import winsound

# Simulated earthquake data: features (seismic readings) and labels (0: no earthquake, 1: earthquake)
# Replace this with actual seismic data
data = np.random.rand(1000, 10)
labels = np.random.randint(2, size=1000)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Simulate real-time earthquake detection
while True:
    new_data = np.random.rand(1, 10)  # Replace with actual data acquisition
    prediction = clf.predict(new_data)
    
    if prediction == 1:
        print("Earthquake detected! Ringing alarm bell...")
        winsound.Beep(500, 2000)  # Use winsound to play a beep sound
    else:
        print("No earthquake detected.")
    
    time.sleep(5)  # Simulate waiting time before next prediction

