# Real-time Object Detection and Counting with OpenCV
This project implements **real-time object detection** and counting using OpenCV, a powerful computer vision library in Python. The program captures frames from a webcam, processes them to detect yellow objects, and draws bounding boxes around them. Additionally, it accurately counts the number of detected yellow objects in the frame, providing a useful tool for various applications such as surveillance, traffic monitoring, and object tracking.

## Key Features
- **Real-time object detection** and counting using OpenCV.
- **Efficient detection** of yellow objects from webcam frames.
- Bounding box **visualization** to highlight detected objects.
- Accurate **counting** of yellow objects with a cooldown period to prevent multiple counts of the same object.
- Versatile application in surveillance, traffic monitoring, and **object tracking**.

## Installation
**1.** Clone the repository
```sh
   git clone https://github.com/your-username/opencv-object-detection.git
```
```sh
  pip install opencv-python numpy pillow
```

**2.** Navigate to the project directory:
```sh
  cd opencv-object-detection
```

**3.** Run the main script:
```sh
 python main.py
```
**4.** A window will open displaying the webcam feed with yellow objects highlighted by bounding boxes. The number of detected yellow objects will be displayed on the frame.

**5.** Press 'q' to quit the application.

  ## Requirements 
- Pyhton 3.x
- OpenCV
- NumPy
- Pillow
