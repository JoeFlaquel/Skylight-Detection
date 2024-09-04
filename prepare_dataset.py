import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

# Paths
image_folder = r'/Users/joeflaquel/Documents/Image Recognition/Images'
output_folder = r'/Users/joeflaquel/Documents/Image Recognition/Processed_Images'
labels_file = r'/Users/joeflaquel/Documents/Image Recognition/labels.csv'

# Load labels
labels = pd.read_csv(labels_file)

# Split the dataset: 80% for training, 20% for validation
train, val = train_test_split(labels, test_size=0.2, random_state=42)

# Create output directories for training and validation sets
os.makedirs(os.path.join(output_folder, 'train/with_skylight'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'train/no_skylight'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'val/with_skylight'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'val/no_skylight'), exist_ok=True)

# Function to copy images to their respective directories
def organize_images(dataframe, set_type):
    for _, row in dataframe.iterrows():
        src = os.path.join(image_folder, row['filename'])
        if row['label'] == 1:
            dst = os.path.join(output_folder, f'{set_type}/with_skylight', row['filename'])
        else:
            dst = os.path.join(output_folder, f'{set_type}/no_skylight', row['filename'])
        shutil.copyfile(src, dst)

# Organize training images
organize_images(train, 'train')

# Organize validation images
organize_images(val, 'val')

print("Data preparation complete. Images organized into training and validation sets.")
