from flask import Flask, request, jsonify
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Define the model architecture
model = models.mobilenet_v2(pretrained=False, num_classes=10)  # Adjust num_classes if needed
model.load_state_dict(torch.load('obstacle_detection_mobilenet.pth', map_location=torch.device('cpu')))
model.eval()  # Set model to evaluation mode

# Mapping from index to class
idx_to_class = {
    0: "chair",
    1: "door",
    2: "fence",
    3: "garbage_bin",
    4: "obstacle",
    5: "plant",
    6: "pothole",
    7: "stairs",
    8: "table",
    9: "vehicle",
}

# Preprocessing for input images
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if an image is provided
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        # Load and preprocess the image
        image_file = request.files['image']
        image = Image.open(io.BytesIO(image_file.read())).convert('RGB')

        input_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        # Make predictions
        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]  # Extract probabilities from batch

        # Get predicted class and its probability
        predicted_idx = probabilities.argmax().item()
        predicted_class = idx_to_class[predicted_idx]
        predicted_probability = probabilities[predicted_idx].item()
        print({'predicted_class': predicted_class, 'predicted_probability': round(predicted_probability, 4)})
        return jsonify({
            'predicted_class': predicted_class,
            'predicted_probability': round(predicted_probability, 4)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
