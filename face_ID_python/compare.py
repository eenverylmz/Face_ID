from deepface import DeepFace

result = DeepFace.verify(
    img1_path="referances/Enver.jpg",
    img2_path="frame.jpg",
    model_name="ArcFace",
    enforce_detection=False
)

print(f"Distance: {result['distance']:.4f}")
print(f"Verified: {result['verified']}")