import requests
import json
import pandas as pd
import base64
from PIL import Image
from io import BytesIO
import os

def request(img_path):
    # define the results folder
    PT_IMAGE_DIR = "D:/python_code/tph-yolov5-main/runs/results"

    # API endpoint
    url = 'http://10.12.55.111:12345/predict'  # Replace with the appropriate URL and port

    # Read the image file in base64 format
    with open(img_path, 'rb') as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    # Prepare input data with the image in base64 format
    input_data = {
        'image_base64': img_base64
    }

    # Send a POST request with the input data
    response = requests.post(url, json=input_data)
    data = json.loads(response.text)
    image_base64 = data.get('image_base64')

    # Decode Base64 data to image bytes
    image_data = base64.b64decode(image_base64)

    # Save the image to a file in the images directory
    image_filename = os.path.join(PT_IMAGE_DIR, 'image.jpg')

    # Check if the image file exists and delete if it does
    if os.path.exists(image_filename):
        os.remove(image_filename)

    with open(image_filename, 'wb') as img_file:
        img_file.write(image_data)
