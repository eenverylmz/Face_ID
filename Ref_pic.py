import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cv2.imwrite("frame.jpg", frame)
    print("Kare başarıyla kaydedildi: frame.jpg")
else:
    print("Kamera görüntüsü alınamadı.")
cap.release()
