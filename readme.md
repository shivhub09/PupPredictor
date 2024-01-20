# PupPredictor

This project is a dog breed classifier that can predict the breed of a dog from an input image. The classifier currently supports four dog breeds: Beagle, Husky, Golden Retriever, and German Shepherd.

## Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Model Training](#model-training)
- [Flask Integration](#flask-integration)
  - [API Endpoint](#api-endpoint)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project consists of a machine learning model for dog breed classification and a Flask web application for integrating the model into a backend. Users can upload images through the web interface, and the model will predict the dog breed based on the provided image.

![image](https://github.com/shivhub09/PupPredictor/assets/114899176/f40fc1ef-82e6-4aa7-a804-e9392c63da08)


## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/dog-breed-classifier.git
    cd dog-breed-classifier
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`. You should see the web interface for uploading images.

3. Choose an image of a dog (Beagle, Husky, Golden Retriever, or German Shepherd) and upload it.

4. The model will make a prediction, and the result will be displayed on the web page.

## Model Training

The machine learning model was trained using a dataset of labeled dog images. The training script and model architecture can be found in the `train_model` directory.

To train the model:

```bash
cd train_model
python train.py
```

This will save the trained model as a file named `dog_breed_classifier_model.h5` in the `models` directory.

## Flask Integration

The Flask application serves as the backend for the dog breed classifier. The integration allows users to interact with the model through a web interface.

### API Endpoint

The Flask app exposes a simple API endpoint for making predictions. You can send a POST request with an image file to the following endpoint:

```
POST http://127.0.0.1:5000/predict
```

Include the image file in the request payload, and the server will respond with a JSON object containing the predicted dog breed.

Example using `requests` in Python:

```python
import requests

url = "http://127.0.0.1:5000/predict"
files = {"image": open("path/to/your/image.jpg", "rb")}
response = requests.post(url, files=files)

print(response.json())
```

### StreamLit WebApp

You can also run and test the model using the streamlit app :
Run the streamlit app using the following command in the terminal

```python
streamlit run app.py
```
![image](https://github.com/shivhub09/PupPredictor/assets/114899176/dba30074-1d33-4f93-b38d-caf2061fdba5)
![image](https://github.com/shivhub09/PupPredictor/assets/114899176/f2f7ebfb-664d-4340-b5d3-848f9baa9e8c)


## Contributing

Feel free to contribute to this project. Please follow the [contributing guidelines](CONTRIBUTING.md) for more information.

## License


