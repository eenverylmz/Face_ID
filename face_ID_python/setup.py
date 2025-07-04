from setuptools import setup, find_packages

setup(
    name="face_id_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "deepface",
        "opencv-python",
        "tensorflow",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'face-id=main:main',  # Eğer main.py içinde main() fonksiyonun varsa
        ],
    },
    author="Enver Yılmaz",
    description="Real-time face recognition using DeepFace and OpenCV",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
