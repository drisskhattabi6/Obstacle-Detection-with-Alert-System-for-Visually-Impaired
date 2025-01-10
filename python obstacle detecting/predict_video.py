import cv2
import requests

# API URL
API_URL = "http://127.0.0.1:5000/predict"

VIDEO_PATH = None
vids = """
    1. vid1.mp4
    2. vid2.mp4
    3. vid3.mp4
"""

# Enter Video file path 
while True:
    try:
        print(vids)
        nbr = int(input("Choose video number to detect obstacls : "))
        if nbr == 1:
            VIDEO_PATH = "vid1.mp4"
        elif nbr == 2:
            VIDEO_PATH = "vid2.mp4"
        elif nbr == 3:
            VIDEO_PATH = "vid3.mp4"
        else:
            print("Please enter a valid number.")
            continue

        video = cv2.VideoCapture(VIDEO_PATH)
        if not video.isOpened():
            print("Error: Unable to open video file.")
        else:
            break
    except Exception as e:
        print(f"Error: {e}")

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
    frame_interval = int(fps * interval)

    frame_count = 0 
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
                        print(f"Time {elapsed_seconds:.2f} seconds prediction:", response_data)

                except Exception as e:
                    print(f"Error processing frame at {elapsed_seconds:.2f} seconds: {e}")

        # Read the next frame
        success, frame = video.read()
        frame_count += 1

    # Release video resources
    video.release()
    print("Processing completed.")

extract_and_predict_frames(VIDEO_PATH, API_URL)
