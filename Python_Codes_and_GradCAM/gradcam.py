import torch
import torch.nn as nn
import cv2
import numpy as np
from ultralytics import YOLO
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

# ==============================
# CONFIG
# ==============================
MODEL_PATH = "best.pt"
IMAGE_PATH = "Talking_left_img_1103_Day.jpg"
IMG_SIZE = 224  # classification input size

# ==============================
# YOLOv8 Wrapper (VERY IMPORTANT)
# ==============================
class YOLOv8ClassifierWrapper(nn.Module):
    def __init__(self, yolo_model):
        super().__init__()
        self.model = yolo_model.model  # actual torch model

    def forward(self, x):
        output = self.model(x)
        if isinstance(output, tuple):
            output = output[0]  # return logits only
        return output


# ==============================
# LOAD MODEL
# ==============================
print("Loading model...")
yolo = YOLO(MODEL_PATH)
wrapped_model = YOLOv8ClassifierWrapper(yolo)

wrapped_model.eval()

for param in wrapped_model.parameters():
    param.requires_grad = True

# ==============================
# SELECT TARGET LAYER
# ==============================
# For YOLOv8 classification, this usually works:
target_layer = wrapped_model.model.model[-2]

# If this fails, uncomment below to inspect layers:
# print(wrapped_model.model.model)

# ==============================
# LOAD & PREPROCESS IMAGE
# ==============================
img_bgr = cv2.imread(IMAGE_PATH)
if img_bgr is None:
    raise ValueError("Image not found. Check IMAGE_PATH.")

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_resized = cv2.resize(img_rgb, (IMG_SIZE, IMG_SIZE))

input_tensor = torch.tensor(img_resized).permute(2, 0, 1).unsqueeze(0).float()
input_tensor = input_tensor / 255.0

# ==============================
# GET PREDICTION
# ==============================
outputs = wrapped_model(input_tensor)

print("Output requires_grad:", outputs.requires_grad)

pred_class = torch.argmax(outputs, dim=1).item()

print(f"Predicted Class Index: {pred_class}")

# ==============================
# GRAD-CAM
# ==============================
cam = GradCAM(
    model=wrapped_model,
    target_layers=[target_layer]
)


targets = [ClassifierOutputTarget(pred_class)]

grayscale_cam = cam(
    input_tensor=input_tensor,
    targets=targets
)[0]

# ==============================
# OVERLAY HEATMAP
# ==============================
visualization = show_cam_on_image(
    img_resized.astype(np.float32) / 255.0,
    grayscale_cam,
    use_rgb=True
)

# Convert back to BGR for OpenCV display
visualization_bgr = cv2.cvtColor(visualization, cv2.COLOR_RGB2BGR)

# cv2.imshow("Grad-CAM", visualization_bgr) # Comment this out
# cv2.waitKey(0)                           # Comment this out
# cv2.destroyAllWindows()                 # Comment this out

# This line will still work regardless of the OpenCV version:
cv2.imwrite("gradcam_output13.jpg", visualization_bgr)
print("Grad-CAM saved as gradcam_output.jpg")