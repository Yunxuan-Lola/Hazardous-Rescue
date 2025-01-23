This repository implements a drone device designed for hazardous area monitoring, human detection, and automated rescue action requests via wireless communication. The system integrates **YOLOv5s** for human recognition and features robust communication protocols to ensure stable image transmission even in challenging environments. The drone captures images, processes them using YOLOv5s, and identifies humans in danger. The results are displayed locally through a GUI and also transmitted to a web page via HTML protocol for real-time updates.

## Features
- **Drone-Based Human Detection**: Uses YOLOv5s for human detection in images captured in hazardous environments.
- **Wireless Communication**: Sends image data and detection results to a web server via wireless communication.
- **Real-Time Display**: Displays detection results locally on a GUI and remotely on a web interface.
- **Rescue Action Requests**: Based on detection, the drone can send automatic rescue requests for humans in danger.
- **Stable Image Transmission**: Implements robust communication protocols for stable image transmission even in adverse conditions.

## System Components

1. **Drone**: The physical drone device equipped with a camera for capturing images in hazardous areas.
2. **YOLOv5s Algorithm**: Deployed on the drone's Intel CPU to perform real-time human detection.
3. **GUI Interface**: Local display of detection results, integrated with the drone for immediate feedback.
4. **Web Interface**: A remote interface that allows users to view the results via HTML protocol.
5. **Communication Protocols**: Developed to ensure reliable transmission of image data over wireless networks.

## Installation

### 1. Clone the repository
```bash
$ git clone https://github.com/yourusername/drone-human-detection.git
$ cd drone-human-detection
```
## 2. Install Dependencies
Make sure to install the required Python libraries:

```bash
$ pip install -r requirements.txt
```
## 3. Convert Labels (If Necessary)
If you're using your own dataset or a specific format, you may need to convert labels into YOLO format. Follow the example below:

```bash
$ python convert_labels.py
Make sure to set the correct path for your dataset in convert_labels.py
```
## 4. Run the Drone Detection Script
Once the setup is complete, you can start the drone-based detection system. This will use the camera to capture images and process them using the YOLOv5s algorithm to detect humans.

```bash
$ python run_drone_detection.py
```
## 5. View Results
The system will display detection results both locally (via the GUI) and on a web interface (accessible through any browser).

- **Local Display**: A GUI will open on the drone system showing real-time results.
- **Web Interface**: View results remotely via a web page by accessing the provided IP address in a browser.

---

## Inference
The YOLOv5s algorithm will be used to detect humans in the images captured by the drone. You can change the model weights to improve detection accuracy or use pre-trained models for faster inference.

### 1. Weights (PyTorch v1.10):
Download the pre-trained weights:
- **weights file**: Google Drive or Baidu Drive

### 2. Run Inference
Use the following script to run inference using YOLOv5s on captured images.

```bash
$ python inference.py --weights ./weights/yolov5s.pt --img-size 640 --source ./input_images --save-txt --save-img
```
Rescue Action System
When a human is detected in the image, the system will:

Trigger an automatic rescue action by sending a request via wireless communication.
Inform operators about the detected human's location and status.

## License
This project is licensed under the **GNU General Public License (GPL) v3.0** - see the [LICENSE](LICENSE) file for details.

---

## References
- YOLOv5
- Transformer Prediction Head (TPH) improvements to YOLOv5

---

## Acknowledgments
Thanks to the authors and contributors of the **YOLOv5** and related research for their pioneering work. If you find this project useful, please cite:

- **TPH-YOLOv5**: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios
- **TPH-YOLOv5++**: Boosting Object Detection on Drone-Captured Scenarios with Cross-Layer Asymmetric Transformer
