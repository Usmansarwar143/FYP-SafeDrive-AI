# 🚗 SafeDrive AI — Real-Time Driver Anomaly Detection on Edge

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi%204-red?style=for-the-badge&logo=raspberry-pi" />
  <img src="https://img.shields.io/badge/Model-YOLOv8n--cls-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Runtime-NCNN-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FYP-Sukkur%20IBA%20University-orange?style=for-the-badge" />
</p>

---

## 📽️ Demo Video

> **Note:** GitHub doesn't natively play MP4 files inline. Click below to watch the demo or download it from the repo.

https://github.com/Usmansarwar143/YOUR_REPO/raw/main/FYP_Video.mp4

> *(Replace `YOUR_REPO` with your actual repository name)*

---

## 📌 Overview

SafeDrive AI is a real-time driver anomaly detection system built to run entirely on the **Raspberry Pi 4** — no cloud, no GPU server, no internet dependency.

The system watches the driver through a camera feed and flags dangerous behaviors like drowsiness, distraction, or other anomalies as they happen. The whole detection pipeline runs locally on the Pi using a compressed YOLOv8n-cls model converted to NCNN format, making it fast enough for real-time inference on constrained hardware.

This was our Final Year Project for the **Bachelor of Engineering in Computer Systems Engineering** at **Sukkur IBA University**, completed in **May 2026**.

---

## 🎯 Problem Statement

Driver inattention is one of the leading causes of road accidents. Existing commercial solutions are either too expensive, cloud-dependent, or require dedicated hardware that isn't practical for most vehicles. We built SafeDrive AI to show that accurate, real-time anomaly detection can run on a $35 single-board computer — making it viable for low-cost deployment in real vehicles.

---

## ✅ Features

- **Real-time inference** on Raspberry Pi 4 with no external compute
- **YOLOv8n-cls** classification model — lightweight, accurate, fast
- **NCNN runtime** for optimized ARM-based edge inference
- **Camera-based pipeline** — plug in a USB/Pi camera and it works
- **Anomaly detection** for driver states: drowsy, distracted, and normal
- **Alert system** to notify when unsafe behavior is detected
- **Fully offline** — no internet connection required during operation

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| ML Model | YOLOv8n-cls (Ultralytics) |
| Inference Runtime | NCNN |
| Edge Hardware | Raspberry Pi 4 (4GB RAM) |
| Camera | Pi Camera / USB Camera |
| Language | Python |
| Model Conversion | NCNN conversion pipeline (PT → ONNX → NCNN) |
| Visualization | GradCAM (for model interpretability) |

---

## 🗂️ Repository Structure

```
SafeDrive-AI/
│
├── Dataset_Training_and_Results/   # Training data, model weights, evaluation results
├── Presentations/                  # FYP presentation decks
├── Progress_Reports/               # Bi-weekly progress reports submitted during FYP
├── Python_Codes_and_GradCAM/       # Main detection code + GradCAM visualizations
├── Synopsis_And_Proposals/         # Initial synopsis and project proposals
├── Thesis_Drafts/                  # Thesis drafts and final write-up
├── FYP_Video.mp4                   # Full demo video (~17 MB)
├── FYP_Video2.mp4                  # Short demo clip (~2.6 MB)
└── README.md
```

---

## ⚙️ How It Works

```
Camera Feed
    ↓
Frame Capture (OpenCV)
    ↓
Preprocessing (Resize, Normalize)
    ↓
YOLOv8n-cls Inference via NCNN
    ↓
Anomaly Classification
  ├── Normal     → No action
  ├── Drowsy     → Alert triggered
  └── Distracted → Alert triggered
    ↓
Real-time Output / Alert
```

### Model Pipeline

The YOLOv8n-cls model was trained on a custom dataset of driver behavior images covering multiple anomaly classes. After training:

1. Model exported from PyTorch (`.pt`) → ONNX
2. ONNX converted to NCNN (`.param` + `.bin`) using `onnx2ncnn`
3. NCNN model loaded directly on Raspberry Pi 4 for inference

NCNN was chosen because it's specifically optimized for ARM architectures with no external dependencies — it runs without TensorFlow, PyTorch, or any heavy framework on the Pi.

---

## 📊 Dataset & Training

- Custom dataset collected and labeled for driver anomaly classes
- Training done on a GPU machine, inference-only on Raspberry Pi
- GradCAM visualizations used to validate that the model focuses on the right regions (face, eyes, head position)
- Full training logs, confusion matrices, and results are in `Dataset_Training_and_Results/`

---

## 🚀 Getting Started

### Hardware Requirements

- Raspberry Pi 4 (2GB RAM minimum, 4GB recommended)
- Pi Camera Module or USB Camera
- MicroSD card (16GB+)
- Power supply (5V 3A)

### Software Requirements

```bash
# On Raspberry Pi OS (64-bit recommended)
pip install opencv-python numpy
# NCNN Python bindings
pip install ncnn
```

### Run the Detection System

```bash
git clone https://github.com/Usmansarwar143/YOUR_REPO.git
cd SafeDrive-AI/Python_Codes_and_GradCAM
python detect.py
```

> Update the model path and camera index in `detect.py` if needed.

---

## 📁 Key Files

| File/Folder | Description |
|---|---|
| `Python_Codes_and_GradCAM/` | Core detection scripts + GradCAM analysis |
| `Dataset_Training_and_Results/` | YOLOv8 training config, weights, metrics |
| `Thesis_Drafts/` | Full academic write-up of the project |
| `Synopsis_And_Proposals/` | Initial project scope and approved synopsis |
| `FYP_Video.mp4` | Primary demo showing live detection on Pi |

---

## 👥 Team

| Name | Role | GitHub |
|------|------|--------|
| **Muhammad Usman** *(Team Leader)* | AI/ML Engineer — Model training, NCNN conversion, edge deployment, system integration | [@Usmansarwar143](https://github.com/Usmansarwar143) |
| **Asma Channa** | Co-developer — Dataset collection, model evaluation, testing, documentation | [@asma-13](https://github.com/asma-13) |
| **Abdul Moiz Barlas** | Co-developer — Data annotation, preprocessing pipeline, progress reporting | — |
| **Kashish Thorani** | Co-developer — Dataset collection, presentation, and project documentation | — |

> **Supervisor:** Dr. Abdul Sattar Chan  
> **Co-Supervisor:** Engr. Umair Ayaz Kamangar  
> **Institution:** Sukkur IBA University — Department of Computer Systems Engineering  
> **Batch:** 2022–2026

---

## 📄 Thesis

The full thesis for SafeDrive AI is available in the `Thesis_Drafts/` folder. It covers:

- Literature review on driver monitoring systems
- Dataset collection and preprocessing methodology
- YOLOv8n-cls model architecture and training details
- NCNN conversion and edge optimization process
- Results, evaluation metrics, and GradCAM analysis
- Limitations and future work

---

## 🔮 Future Work

- Add sound-based alerts (buzzer/speaker integration on Pi)
- Expand anomaly classes (phone usage, eating, smoking)
- Train on a larger, more diverse dataset
- Explore quantized INT8 inference for even faster speeds
- Build a mobile companion app for alert notifications

---

## 📜 License

This project is developed as an academic Final Year Project at Sukkur IBA University. Feel free to reference or build on it — just give credit.

---

## 🙏 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for the base model architecture
- [NCNN](https://github.com/Tencent/ncnn) by Tencent for the edge inference framework
- Sukkur IBA University faculty for guidance throughout the project

---

<p align="center">Built with Python, YOLOv8, NCNN, and a Raspberry Pi 4 &nbsp;|&nbsp; Sukkur IBA University &nbsp;|&nbsp; 2026</p>
