import cv2
import requests
import io
from PIL import Image

# API URL
API_URL = "http://127.0.0.1:5000/predict"

# Video file path
VIDEO_PATH = "vid3.mp4"
def extract_and_predict_frames(video_path, api_url, interval=2):
    """
    Extract frames from the video at the specified interval (in seconds)
    and send them to the prediction API.
    
    Parameters:
    - video_path: Path to the video file.
    - api_url: URL of the prediction API.
    - interval: Time interval (in seconds) between frames to process.
    """
    # Open the video file
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error: Unable to open video file.")
        return

    # Get video frame rate and calculate interval in terms of frames
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)  # Frames to skip for the given time interval

    frame_count = 0  # To track the frame number
    success, frame = video.read()

    while success:
        # Check if the current frame is at the desired interval
        if frame_count % frame_interval == 0:
            # Calculate the elapsed time in seconds
            elapsed_seconds = frame_count / fps

            # Save the frame to a temporary file
            frame_filename = "temp_frame.jpg"
            cv2.imwrite(frame_filename, frame)

            # Send the frame to the prediction API
            with open(frame_filename, "rb") as image_file:
                files = {"image": image_file}
                try:
                    response = requests.post(api_url, files=files)
                    response_data = response.json()

                    if response_data['predicted_probability'] > 0.8 :
                        # Print the prediction result with elapsed seconds
                        print(f"Time {elapsed_seconds:.2f} seconds prediction:", response_data)

                except Exception as e:
                    print(f"Error processing frame at {elapsed_seconds:.2f} seconds: {e}")

        # Read the next frame
        success, frame = video.read()
        frame_count += 1

    # Release video resources
    video.release()
    print("Processing completed.")

# Run the function
extract_and_predict_frames(VIDEO_PATH, API_URL)
