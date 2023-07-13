from flask import Flask, request, jsonify
import PIL.Image
import io
import numpy as np
import base64
from keras.models import load_model

app = Flask(__name__)

# Load model
model = load_model('model.h5')


@app.route('/infer', methods=['POST'])
def infer_image():
    try:
        if 'image' not in request.files:
            return jsonify({'code': 400, 'data': 'No image file provided'}), 400

        image_file = request.files['image']

        # Convert file to PIL image
        image = PIL.Image.open(image_file.stream)

        # Preprocess the image to fit the model input requirements
        processed_image = preprocess(image)

        # Predict
        prediction = model.predict(processed_image)

        # Get the index of the maximum prediction
        max_prediction_index = np.argmax(prediction)

        # Return the prediction as JSON
        return jsonify({'code': 200, 'data': int(max_prediction_index)}), 200
    except Exception as e:
        # If an error occurred during prediction, return an error response
        return jsonify({'code': 500, 'data': 'Prediction failed'}), 500


def preprocess(image):
    # Update the preprocess function to handle the incoming PIL image
    image = image.resize((28, 28))
    image = np.array(image).reshape(1, 28, 28, 1)  # Assuming the model takes input shape of (1, 28, 28, 1)
    image = image.astype('float32') / 255.0  # Assuming the model input values are normalized between 0 and 1
    return image


if __name__ == '__main__':
    app.run()
