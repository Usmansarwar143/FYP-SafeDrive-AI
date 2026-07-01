import os
import cv2
from tqdm import tqdm

input_folder = r"train\Drowsy"
output_folder = r"train\Drowsy_Resized_Zoom"

target_width = 640
target_height = 680

os.makedirs(output_folder, exist_ok=True)

target_ratio = target_width / target_height

for filename in tqdm(os.listdir(input_folder)):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is None:
            continue

        h, w = img.shape[:2]
        current_ratio = w / h

        # If image is too wide
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            x_start = (w - new_w) // 2
            cropped = img[:, x_start:x_start+new_w]

        # If image is too tall
        else:
            new_h = int(w / target_ratio)
            y_start = (h - new_h) // 2
            cropped = img[y_start:y_start+new_h, :]

        resized = cv2.resize(cropped, (target_width, target_height),
                             interpolation=cv2.INTER_AREA)

        save_path = os.path.join(output_folder, filename)
        cv2.imwrite(save_path, resized)

print("All images resized using zoom (center crop) method.")