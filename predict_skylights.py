import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Paths
image_folder = r'/Users/joeflaquel/Documents/Image Recognition/Images'
model_path = r'/Users/joeflaquel/Documents/Image Recognition/skylight_detection_model.keras'
output_file = r'/Users/joeflaquel/Documents/Image Recognition/predictions.csv'

# Load the trained model
model = load_model(model_path)

# Prepare a list to store the results
results = []

# Supported image extensions
valid_extensions = ('.jpg', '.jpeg', '.png')

# Iterate over each image in the new dataset
for img_name in os.listdir(image_folder):
    if img_name.lower().endswith(valid_extensions):  # Filter for image files
        img_path = os.path.join(image_folder, img_name)
        try:
            img = image.load_img(img_path, target_size=(224, 224))  # Ensure the image size matches the input size of the model
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            img_array /= 255.0  # Normalize the image to the [0, 1] range

            # Run the prediction
            prediction = model.predict(img_array)

            # Determine if skylight is present (you can adjust the threshold if needed)
            skylight_present = 1 if prediction >= 0.5 else 0

            # Append the result to the list
            results.append([img_name, skylight_present])

        except Exception as e:
            print(f"Error processing image {img_name}: {e}")
            continue  # Skip to the next file

# Save the results to a CSV file
import pandas as pd
df = pd.DataFrame(results, columns=['filename', 'skylight_present'])
df.to_csv(output_file, index=False)

print("Predictions complete. Results saved to", output_file)
