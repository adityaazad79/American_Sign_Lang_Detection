# American Sign Language Detection using YOLOv7

- This project aims to detect American Sign Language (ASL) gestures using the YOLOv7 object detection model.

- The application is built using Flask for the backend and integrates with YOLOv7 for real-time and image-based ASL detection.

## Table of Contents
- [Running the Application](#running-the-application)

## Running the Application

The Flask application (`app.py`) handles image uploads and real-time detection.

Install the dependencies

```
pip install -r requirements.txt
```

Join the spilitted model (Splitted due to GitHub size limit constraint of 50 MB)
```
python yolov7/join_model.py
```

Run the Flask application to start the server.

```
python app.py
```

Citations:

[1] https://github.com/augmentedstartups/yolov7.git

[2] https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
