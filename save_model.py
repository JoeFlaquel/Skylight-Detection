from tensorflow.keras.models import load_model

# Load the model you trained
model = load_model('skylight_detection_model.h5')

# Save the model in the native Keras format
model.save('skylight_detection_model.keras')

print("Model saved in Keras format.")
