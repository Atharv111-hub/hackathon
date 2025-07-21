import cv2
import os

def extract_faces_from_video(video_path, output_dir):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success, image = vidcap.read()
    while success:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = image[y:y + h, x:x + w]
            face = cv2.resize(face, (299, 299))
            cv2.imwrite(os.path.join(output_dir, f"frame{count}_face.jpg"), face)
        success, image = vidcap.read()
        count += 1

# Example usage:
# extract_faces_from_video("video.mp4", "data/train/real/")
