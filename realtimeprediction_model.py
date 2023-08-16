while True:
    new_data = np.random.rand(1, 10)  # Replace with actual data acquisition
    
    # Predict using the loaded model
    prediction = model.predict(new_data)
    
    if prediction == 1:
        print("Earthquake detected! Ringing alarm bell...")
        winsound.Beep(500, 2000)  # Use winsound to play a beep sound
    else:
        print("No earthquake detected.")
    
    time.sleep(5)  # Simulate waiting time before next prediction
