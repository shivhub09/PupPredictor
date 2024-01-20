from flask import Flask, request, jsonify
import tensorflow as tf
import cv2
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model('golden_trio.h5')

breed_labels = ["beagle", "German Shepherd", "Golden Retriever", "Husky"]

@app.route('/', methods=['POST'])
def predict_breed():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image_file = request.files['image']

    # Read the image using OpenCV
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Resize and preprocess the image
    resized_image = cv2.resize(image, (256, 256))
    resized_image = np.expand_dims(resized_image, axis=0)
    resized_image = resized_image.astype(np.float32) / 255.0

    # Make predictions using the loaded model
    predictions = model.predict(resized_image)
    max_index = np.argmax(predictions[0])
    predicted_breed = breed_labels[max_index]

    return jsonify({'breed': predicted_breed})

if __name__ == '__main__':
    app.run(debug=True)
