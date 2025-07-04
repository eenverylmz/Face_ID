import threading
import cv2
import os
from deepface import DeepFace

# Log uyarılarını kapat
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
distance = 1.0


# ArcFace modelini yükle
model_name = "ArcFace"
model = DeepFace.build_model(model_name)
threshold = 0.68

def check_face(frame):
    global face_match, distance
    try:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = DeepFace.verify(
            img1=frame_rgb,
            img2_path="referances/Enver.jpg",
            model_name=model_name,  
            enforce_detection=False
        )
        distance = result["distance"]
        face_match = distance < threshold
        print(f"[INFO] Distance: {distance:.4f} - Match: {face_match}")
    except Exception as e:
        print(f"[ERROR] Face match error: {e}")
        face_match = False
        distance = 1.0

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Camera Not Found")
        break

    # Thread çalıştır
    if counter % 45 == 0:
        threading.Thread(target=check_face, args=(frame.copy(),)).start()
    counter += 1

    # Renk kodu
    if distance < 0.4:
        color = (0, 255, 0)  # Strong match
    elif distance < threshold:
        color = (0, 255, 255)  # Orta seviye
    else:
        color = (0, 0, 255)  # Fail

    # GUI yazılarını ekle
    cv2.putText(frame, f"Distance: {distance:.4f}", (20, 420), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    msg = "MATCH!" if face_match else "MATCH FAIL!"
    cv2.putText(frame, msg, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 2, color, 3)

    cv2.imshow("video", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
