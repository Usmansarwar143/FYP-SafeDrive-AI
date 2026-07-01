import os
from PIL import Image

# Input & output paths
input_dir = "dataset"
output_dir = "Compressed_dataset"

# Compression quality (1-100) → lower = smaller size
quality = 70  

# Go through train/val and class folders
for split in ["train", "val"]:
    split_input = os.path.join(input_dir, split)
    split_output = os.path.join(output_dir, split)
    
    for class_folder in os.listdir(split_input):
        class_input = os.path.join(split_input, class_folder)
        class_output = os.path.join(split_output, class_folder)
        
        os.makedirs(class_output, exist_ok=True)
        
        for file in os.listdir(class_input):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(class_input, file)
                output_path = os.path.join(class_output, file)
                
                try:
                    img = Image.open(input_path)
                    img.save(output_path, optimize=True, quality=quality)
                except Exception as e:
                    print(f"⚠️ Could not compress {input_path}: {e}")
                    
print("\n🎉 Compression complete! Check 'Compressed_dataset/'")
