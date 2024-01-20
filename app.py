from PIL import Image
import streamlit as st
import requests
import io

api_url = "http://127.0.0.1:5000/"

def main():
    st.title("Image Upload with Streamlit")

    # File uploader component
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image with adjusted size
        st.image(uploaded_file, caption="Uploaded Image", width=400)

        # Process the uploaded image (optional)
        image = Image.open(uploaded_file)

        # Convert the PIL Image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes = image_bytes.getvalue()

        # Create a file-like object to upload with requests
        files = {'image': ('image.jpg', image_bytes, 'image/jpeg')}

        # Send the image to the API
        response = requests.post(api_url, files=files)

        if response.status_code == 200:
            result = response.json()
            st.write("The Dog in the uploaded image is of the breed:", result["breed"])
        else:
            st.write(f"Error: {response.text}")

if __name__ == "__main__":
    main()
