import cv2
import os

def flip_images_in_folder(input_folder, output_folder):
    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if it's a file and has an image extension
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            # Read image
            img = cv2.imread(input_path)
            if img is None:
                print(f"Skipping {filename}: Not a valid image.")
                continue

            # Flip horizontally (right-to-left)
            flipped_img = cv2.flip(img, 1)

            # Save to output folder with the same filename
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, flipped_img)
            print(f"Flipped and saved: {output_path}")

# Example usage
input_folder = "c9"     # Folder containing original images
output_folder = "Distracted"  # Folder to save flipped images

flip_images_in_folder(input_folder, output_folder)
