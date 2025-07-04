# 🔐 Face_ID Python Project

This project uses Python and the DeepFace library to perform **real-time face verification**. It compares a live video feed from your webcam with a reference image to determine whether the faces match.

## 🚀 Features

- 🎥 Real-time webcam support using OpenCV
- 🧠 Deep learning-based face recognition (ArcFace model)
- 🧵 Background face verification using threading
- ✅ Displays distance score and match result on screen
- 🌈 Color-coded visual feedback (green/yellow/red)
- 🔕 Suppresses TensorFlow warnings for cleaner logs

---

## 🛠 Requirements

The following Python libraries are required:

- `opencv-python`
- `deepface`
- `tensorflow`
- `numpy`


To install all dependencies:

```bash
pip install -r requirements.txt

Face_ID_Python/
│
├── referances/
│   └── Your_photo_here          # Reference face image
├── main.py                # Main application script
└── README.md              # This file
