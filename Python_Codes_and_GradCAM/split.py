import os
import random
import shutil

# Input class folders
input_folders = ["Using_Phone", "Drinking", "Distracted", "Neutral", "Reaching_Behind"]

# Output structure
output_dir = "dataset"
train_dir = os.path.join(output_dir, "train")
val_dir = os.path.join(output_dir, "val")

# Train/Val split ratio
train_ratio = 0.8

# Make directories
for folder in input_folders:
    os.makedirs(os.path.join(train_dir, folder), exist_ok=True)
    os.makedirs(os.path.join(val_dir, folder), exist_ok=True)

# Split each class
for folder in input_folders:
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    random.shuffle(files)
    
    split_index = int(len(files) * train_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]
    
    # Copy train files
    for f in train_files:
        shutil.copy(os.path.join(folder, f), os.path.join(train_dir, folder, f))
    
    # Copy val files
    for f in val_files:
        shutil.copy(os.path.join(folder, f), os.path.join(val_dir, folder, f))
    
    print(f"✅ {folder}: {len(train_files)} train, {len(val_files)} val")

print("\n🎉 Dataset prepared successfully in 'dataset/' with 80% train and 20% val.")
