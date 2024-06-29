import os
from PIL import Image

def create_yolo_labels(image_folder, label_folder, class_number=0):
    # Ensure the label folder exists
    os.makedirs(label_folder, exist_ok=True)

    # Loop through all files in the image folder
    for filename in os.listdir(image_folder):
        if filename.endswith('jpg'):
            # Open the image to get its dimensions
            image_path = os.path.join(image_folder, filename)
            with Image.open(image_path) as img:
                width, height = img.size

            # YOLO format: class_number center_x center_y width height
            # Since the bounding box is the entire image, center_x and center_y are 0.5, and width and height are 1.0
            yolo_label = f"{class_number} 0.5 0.5 1.0 1.0\n"

            # Write the label to a corresponding text file
            new_file_name = int(os.path.splitext(filename)[0]) + 2084
            label_filename = str(new_file_name) + '.txt'
            label_path = os.path.join(label_folder, label_filename)
            new_image_path = os.path.join(image_folder, str(new_file_name) + '.jpg')
            os.rename(image_path, new_image_path)
            with open(label_path, 'w') as label_file:
                label_file.write(yolo_label)

            print(f"Label for {filename} created at {label_path}")

# Usage example
image_folder = r'C:\Users\kwasi\OneDrive\Pulpit\AGH\semestr4\CUDA\GTSDB\in_jpg_all\FullIJCNN2013\two\42'
label_folder = r'C:\Users\kwasi\OneDrive\Pulpit\AGH\semestr4\CUDA\GTSDB-YOLO\labels_2'
create_yolo_labels(image_folder, label_folder, 24)
