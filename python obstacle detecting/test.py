import requests
import os
import io
from PIL import Image
from flask import Flask, request, jsonify

url = 'http://127.0.0.1:5000/predict'
image_path = 'img1.jpg'

IMAGE_PATH = os.path.join('imgs', image_path)


if os.path.exists(IMAGE_PATH):
    with open(IMAGE_PATH, 'rb') as img:
        # files = {'image': img}
        # response = requests.post(url, files=files)
        image = Image.open(img).convert('RGB')
        image.show()  # This will display the image
    # print(response.json())
else:
    print(f"File not found: {IMAGE_PATH}")
