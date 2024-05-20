# Face Recognition Attendance System

This project is a Face Recognition Attendance System that captures real-time video from a webcam, detects faces, and matches them with reference images to log attendance. The attendance is recorded in an Excel file with timestamps.

## Requirements

- Python 3.6+
- OpenCV
- face_recognition
- openpyxl
- numpy

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Prince29chouhan/Face_attendence_project.git
    cd face-recognition-attendance
    ```

2. **Install Required Libraries:**
    ```bash
    pip install opencv-python face_recognition openpyxl numpy
    ```

3. **Prepare Reference Face Images:**
    - Create a directory named `reference_faces`.
    - Add reference images to this directory. Each image file should be named after the person in the image (e.g., `john_doe.jpg`).

## Usage

1. **Running the Script:**
    ```bash
    python face_recognition_attendance.py
    ```
    - The script initializes the webcam and starts capturing frames.
    - It detects faces in each frame and compares them with the reference images.
    - If a match is found, it logs the person's name and the current timestamp in an Excel file (`attendance.xlsx`).

2. **Stopping the Capture:**
    - Press the `q` key to stop the capture and exit the script.

## Project Overview

### Load Reference Face Images

The script loads reference face images from the `reference_faces` directory and encodes them for comparison.

### Initialize the Excel File

An Excel workbook is created to log attendance, with columns for names and timestamps.

### Initialize the Camera and Capture Frames

The script captures frames from the webcam and processes them to detect and recognize faces.

### Save Attendance Data

Matched faces are logged in an Excel file with the current timestamp.





