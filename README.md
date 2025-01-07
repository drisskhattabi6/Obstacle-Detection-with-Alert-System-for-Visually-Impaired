# Obstacles Detection and Alert System for Visually Impaired  

### Using Deep Learning and Node-RED  

## Overview  
This project introduces a robust solution to assist visually impaired individuals in navigating their environment using an obstacle detection and alert system. The system combines:  
- **Deep Learning Models**: A Convolutional Neural Network (CNN) trained from scratch and fine-tuned MobileNetV2 for obstacle classification.  
- **Alert System**: Real-time audio feedback using Node-RED, integrated with a Flask API to process predictions.  

## Features  
- Custom-trained deep learning models for obstacle classification.  
- Real-time alerts through audio guidance for identified obstacles.  
- Flask API for model prediction and integration with Node-RED for automation.  

---

## Getting Started  

### Prerequisites  
Ensure you have the following installed on your system:  
- Python 3.8+  
- Node.js and Node-RED  
- pip (Python package manager)  
- Flask  
- Required Python libraries (see `requirements.txt`)  

---

### Installation  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/yourusername/obstacle-detection-alert-system.git  
   cd obstacle-detection-alert-system  
   ```  

2. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Download Pretrained Model**  
   - Download the MobileNetV2 pretrained model from [link-to-model] and place it in the `models` directory.  

---

## Running the System  

### 1. Running the Flask API  
The Flask API serves as the backend for processing images and returning obstacle classifications.  

**Steps:**  
1. Navigate to the `api` directory:  
   ```bash  
   cd api  
   ```  
2. Start the Flask server:  
   ```bash  
   python app.py  
   ```  
3. The API will start running at `http://127.0.0.1:5000`.  

---

### 2. Setting Up and Running Node-RED  
The Node-RED flow is responsible for integrating the API predictions with the alert system.  

**Steps:**  
1. Install Node-RED globally if you haven’t already:  
   ```bash  
   npm install -g node-red  
   ```  
2. Launch Node-RED:  
   ```bash  
   node-red  
   ```  
3. Open the Node-RED interface at `http://127.0.0.1:1880`.  
4. Import the provided Node-RED flow file (`node-red-flow.json`) into Node-RED.  
   - Click on the menu (top-right corner) → "Import" → "Clipboard".  
   - Paste the content of `node-red-flow.json` and deploy the flow.  
5. Ensure that the Node-RED flow triggers the Flask API and processes responses for the audio alerts.  

---

### 3. Running the Alert System  
The alert system triggers audio notifications based on the API's predictions.  

1. Verify the Flask API and Node-RED are running.  
2. Test the system by uploading an obstacle image through the Node-RED dashboard or directly via the API.  
3. Ensure the audio feedback plays automatically for detected obstacles.  

---

## Project Structure  
```plaintext  
obstacle-detection-alert-system/  
├── api/  
│   ├── app.py            # Flask API for predictions  
│   ├── models/           # Pretrained MobileNetV2 and CNN models  
│   └── requirements.txt  # Python dependencies  
├── node-red-flow.json    # Node-RED flow configuration  
├── data/  
│   └── dataset/          # Custom obstacle classification dataset  
└── README.md             # Project documentation  
```  

---

## References  
1. Mark Sandler et al., *MobileNetV2: Inverted Residuals and Linear Bottlenecks*.  
2. Node-RED Documentation, [Node-RED Official Site](https://nodered.org/docs/).  
3. Shorten, Connor, et al., *A Survey on Image Data Augmentation for Deep Learning*.  

---

## License  
This project is licensed under the MIT License. See the `LICENSE` file for details.  

## Acknowledgments  
Special thanks to the contributors and the Kaggle community for providing datasets and resources that made this project possible.  
