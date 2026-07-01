import cv2
import matplotlib.pyplot as plt

# ==================================================
# PASTE YOUR IMAGE PATHS HERE
# ==================================================

image_paths = [
    r"distracted.jpg",
    r"drinking.jpg",
    r"drowsy.jpg",
    r"phone.jpg",
    r"gradcam_distracted.jpg",
    r"gradcam_drinking.jpg",
    r"gradcam_drowsy.jpg",
    r"gradcam_phone.jpg"
]

# Labels
labels = [
    "Distracted",
    "Drinking",
    "Drowsy",
    "Phone",
    "GradCam Distracted",
    "GradCam Drinking",
    "GradCam Drowsy",
    "GradCam Phone"
]

# Define a uniform size for all images (Width, Height)
TARGET_SIZE = (300, 300) 

# ==================================================
# CREATE GRID
# ==================================================

fig, axes = plt.subplots(2, 4, figsize=(18, 8))
axes = axes.flatten()

for i in range(8):

    img = cv2.imread(image_paths[i])

    if img is None:
        print(f"Could not load: {image_paths[i]}")
        continue

    # 1. Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 2. Resize to ensure uniform dimensions in the grid
    img = cv2.resize(img, TARGET_SIZE, interpolation=cv2.INTER_AREA)

    axes[i].imshow(img)
    axes[i].set_title(
        labels[i],
        fontsize=11,
        fontweight='bold',
        y=-0.18
    )
    axes[i].axis("off")

plt.subplots_adjust(
    wspace=0.03,
    hspace=0.15
)

plt.savefig(
    "gradcam_visualization.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print("Saved as gradcam_visualization.png")