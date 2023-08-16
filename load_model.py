import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import time
import winsound

# Load the trained model
model = RandomForestClassifier()  # Replace with your trained model

# Load the CSV data
data = pd.read_csv("earthquake_data.csv")

# Extract features and labels
X = data.drop("label", axis=1).values
y = data["label"].values
