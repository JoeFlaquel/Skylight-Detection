Skylight Detection using Satellite Images

Overview
    This project aims to detect skylights in satellite images using a convolutional neural network (CNN) model. The system allows users to label satellite images, train a machine learning model, and use the trained model to predict the presence of skylights in new satellite images. The project includes scripts for data processing, model training, and predictions.

Features
    Image Labeling: Easily label satellite images as "skylight" or "no skylight."
    Model Training: Train a CNN model to detect skylights based on labeled images.
    Prediction: Use the trained model to predict skylights in new satellite images.
    Image Augmentation: Optional data augmentation for improving model performance.

Project Structure
    labeling_script.py: Script for labeling images and storing labels in a CSV file.
    prepare_dataset.py: Script to process images and organize them into training and validation sets.
    train_model.py: Script to train the CNN model.
    predict_skylights.py: Script to predict skylights in new satellite images using the trained model.
    augment_images.py: Script to augment images by flipping them for better training.
    skylight_detection_model.keras: The trained model in Keras format.
    README.md: This file.

Installation
    Prerequisites
        Python 3.8+
        TensorFlow
        Pillow (PIL)
        Scikit-learn
        Git LFS (for handling large files)

Steps
    Clone the repository:
        git clone https://github.com/JoeFlaquel/skylight-detection.git
    
    Navigate to the project directory:
        cd skylight-detection
    
    Set up a virtual environment and install dependencies:
        python3 -m venv myenv
        source myenv/bin/activate
        pip install -r requirements.txt

    Make sure to pull down the model files if needed by using Git LFS.

Data
    Make sure to place your satellite images in the appropriate folder for training or predictions. Refer to prepare_dataset.py for how the project expects the images to be structured.

Usage
    Image Labeling
    Use the labeling_script.py to label images as containing skylights or not. Run the following command:
    python labeling_script.py

Preparing the Dataset
    Run the following script to split the dataset into training and validation sets:

    python prepare_dataset.py

Model Training
    To train the model, use:
    python train_model.py

Predicting Skylights
    To use the trained model to detect skylights in new images:
    python predict_skylights.py

Augmenting Images
    To perform image augmentation, such as flipping images:
    python augment_images.py

Contributions
Feel free to open issues and submit pull requests if you want to contribute to this project. Suggestions for improvements are always welcome.