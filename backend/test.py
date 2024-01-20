import requests

api_url = "http://127.0.0.1:5000/"

image_path = 'beagle.jpg'

with open(image_path, 'rb') as file:
    files = {'image': (image_path, file, 'image/jpeg')}
    response = requests.post(api_url, files=files)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.text}")
