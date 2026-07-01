import os
import random
import shutil

# Folders
folders = ["Texting_left", "Texting_right", "Talking_left", "Talking_right"]
output_folder = "Using_Phone"

# Total images required
total_images = 2346
images_per_folder = total_images // len(folders)  # 586 per folder

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

for folder in folders:
    # Get all images in the folder
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    # Randomly select required number of images
    selected_files = random.sample(files, images_per_folder)
    
    for file in selected_files:
        src = os.path.join(folder, file)
        dst = os.path.join(output_folder, f"{folder}_{file}")  # keep unique names
        shutil.copy(src, dst)

print(f"✅ Successfully created '{output_folder}' with {total_images} images ({images_per_folder} from each folder).")
