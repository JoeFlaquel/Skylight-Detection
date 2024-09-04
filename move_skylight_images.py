import os
import shutil

# Path to the folder with all images
source_folder = r'/Users/joeflaquel/Documents/Image Recognition/Images'

# Path to the folder where skylight images will be moved
destination_folder = r'/Users/joeflaquel/Documents/Image Recognition/Skylight_Images'

# List of filenames of images that contain skylights
skylight_filenames = [
     'Satellite_image_41.73821_-71.30494.jpg',
    'Satellite_image_41.73821_-71.30894.jpg',
    'Satellite_image_41.73821_-71.32374.jpg',
    'Satellite_image_41.73821_-71.32414.jpg',
    'Satellite_image_41.73821_-71.32734.jpg',
    'Satellite_image_41.73861_-71.31414.jpg',
    'Satellite_image_41.73861_-71.32134.jpg',
    'Satellite_image_41.73861_-71.32254.jpg',
    'Satellite_image_41.73861_-71.32374.jpg',
    'Satellite_image_41.73861_-71.33014.jpg',
    'Satellite_image_41.73901_-71.30494.jpg',
    'Satellite_image_41.73901_-71.31414.jpg',
    'Satellite_image_41.73901_-71.32014.jpg',
    'Satellite_image_41.73901_-71.32094.jpg',
    'Satellite_image_41.73901_-71.32134.jpg',
    'Satellite_image_41.73901_-71.32294.jpg',
    'Satellite_image_41.73901_-71.32334.jpg',
    'Satellite_image_41.73901_-71.32454.jpg',
    'Satellite_image_41.73901_-71.32494.jpg',
    'Satellite_image_41.73901_-71.32534.jpg',
    'Satellite_image_41.73901_-71.32614.jpg',
    'Satellite_image_41.73901_-71.32654.jpg',
    'Satellite_image_41.73901_-71.32894.jpg',
    'Satellite_image_41.73941_-71.30534.jpg',
    'Satellite_image_41.73941_-71.31054.jpg',
    'Satellite_image_41.73941_-71.31134.jpg',
    'Satellite_image_41.73941_-71.31214.jpg',
    'Satellite_image_41.73941_-71.31254.jpg',
    'Satellite_image_41.73941_-71.31694.jpg',
    'Satellite_image_41.73941_-71.32014.jpg',
    'Satellite_image_41.73941_-71.32134.jpg',
    'Satellite_image_41.73941_-71.32174.jpg',
    'Satellite_image_41.73941_-71.32214.jpg',
    'Satellite_image_41.73941_-71.32374.jpg',
    'Satellite_image_41.73941_-71.32534.jpg',
    'Satellite_image_41.73981_-71.30574.jpg',
    'Satellite_image_41.73981_-71.31494.jpg',
    'Satellite_image_41.73981_-71.32134.jpg',
    'Satellite_image_41.73981_-71.32174.jpg',
    'Satellite_image_41.73981_-71.32494.jpg',
    'Satellite_image_41.74021_-71.30894.jpg',
    'Satellite_image_41.74021_-71.31214.jpg',
    'Satellite_image_41.74021_-71.31294.jpg',
    'Satellite_image_41.74021_-71.32574.jpg',
    'Satellite_image_41.74061_-71.30534.jpg',
    'Satellite_image_41.74061_-71.31174.jpg',
    'Satellite_image_41.74061_-71.32294.jpg',
    'Satellite_image_41.74101_-71.30774.jpg',
    'Satellite_image_41.74101_-71.31094.jpg',
    'Satellite_image_41.74101_-71.31174.jpg',
    'Satellite_image_41.74101_-71.31934.jpg',
    'Satellite_image_41.74101_-71.32414.jpg',
    'Satellite_image_41.74101_-71.32454.jpg',
    'Satellite_image_41.74141_-71.31214.jpg',
    'Satellite_image_41.74141_-71.32414.jpg',
    'Satellite_image_41.74141_-71.32494.jpg',
    'Satellite_image_41.74181_-71.31334.jpg',
    'Satellite_image_41.74181_-71.31414.jpg',
    'Satellite_image_41.74181_-71.31894.jpg',
    'Satellite_image_41.74181_-71.32334.jpg',
    'Satellite_image_41.74181_-71.32374.jpg',
    'Satellite_image_41.74221_-71.31294.jpg',
    'Satellite_image_41.74221_-71.31334.jpg',
    'Satellite_image_41.74221_-71.31894.jpg',
    'Satellite_image_41.74221_-71.32374.jpg',
    'Satellite_image_41.74221_-71.32734.jpg'
    # Add more filenames here
]

# Ensure the destination directory exists
os.makedirs(destination_folder, exist_ok=True)

# Iterate through the list of skylight filenames
for filename in skylight_filenames:
    # Construct the full file path
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    
    # Check if the file exists in the source directory
    if os.path.exists(source_path):
        # Move the file to the destination directory
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
    else:
        print(f"File not found: {filename}")

print("All skylight images have been moved.")
