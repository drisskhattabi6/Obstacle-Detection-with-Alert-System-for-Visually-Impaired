import cv2
import requests
import os

# API URL
API_URL = "http://127.0.0.1:5000/predict"

IMAGES = """
    enter image name to detect objects:
    like those :  img1.jpg, img2.jpg, img3.jpg ...
"""

IMAGE_PATH = None

# Choose an image file to process
while True:
    try:
        print(IMAGES)
        IMAGE_NAME  = input("=> ")
        IMAGE_PATH = os.path.join('imgs', IMAGE_NAME)
        image = cv2.imread(IMAGE_PATH)
        if image is None:
            print("Error: Unable to load image file.")
        else:
            break
    except Exception as e:
        print(f"Error: {e}")

def send_image_to_api(image_path, api_url):
    """
    Send the selected image to the prediction API and display the response.

    Parameters:
    - image_path: Path to the image file.
    - api_url: URL of the prediction API.
    """
    try:
        # Open the image file in binary mode
        with open(image_path, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(api_url, files=files)
            response_data = response.json()

            # Display the response
            if response.status_code == 200:
                print("Prediction result:", response_data)
            else:
                print("Error: API returned an error:", response.text)
    except Exception as e:
        print(f"Error sending image to API: {e}")

# Send the selected image to the API
send_image_to_api(IMAGE_PATH, API_URL)
