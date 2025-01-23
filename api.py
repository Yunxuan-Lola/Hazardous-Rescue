# Dependencies
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
import os
import sys

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        print(json_)
        query = pd.get_dummies(pd.DataFrame(json_))

        prediction = list(lr.predict(query))

        return jsonify({'prediction': str(prediction)})
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    app.run(port=port, debug=True)


# example
# ... (previous imports and code)

# Load the model once and keep it in memory
model = None


def load_model():
    global model
    weights_path = ROOT / 'yolov5s.pt'  # Adjust this based on your model
    opt = parse_opt()
    check_requirements(exclude=('tensorboard', 'thop'))
    model = run(**vars(opt))


def perform_inference(image):
    global model
    # Ensure the model is loaded
    if model is None:
        load_model()

    # Perform inference using the loaded model
    # Modify this based on how your model performs inference
    # For example, you might need to preprocess the image appropriately
    # and then pass it to the model for prediction.
    # Replace this with your actual inference logic
    # For now, we'll return a dummy result.
    dummy_result = np.zeros((100, 100, 3), dtype=np.uint8)

    return dummy_result


@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        image_base64 = json_.get('image_base64', '')
        image_data = base64.b64decode(image_base64)

        # Perform inference
        result_image = perform_inference(image_data)

        # Convert the resulting image to base64
        _, img_encoded = cv2.imencode('.png', result_image)
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')

        return jsonify({'image_base64': img_base64})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # Command-line input for port
    except:
        port = 12345  # Default port if not provided

    app.run(host='10.16.204.126', port=port, debug=True)
