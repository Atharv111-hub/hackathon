from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

model = load_model("xception_deepfake.h5")
img_path = "example_face.jpg"

def predict(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.
    pred = model.predict(img_array)
    return "Fake" if pred[0][0] > 0.5 else "Real"

result = predict(img_path)
print(f"{img_path}: {result}")
