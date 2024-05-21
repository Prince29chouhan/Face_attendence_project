# Face Recognition System

This project demonstrates a Face Recognition System that compares faces from test images with a set of reference images, identifying the best match for each test face.

## Requirements

- Python 3.6+
- OpenCV
- face_recognition
- numpy

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/face-recognition-system.git
    cd face-recognition-system
    ```

2. **Install Required Libraries:**
    ```bash
    pip install opencv-python face_recognition numpy
    ```

3. **Prepare Reference and Test Face Images:**
    - Create a directory named `reference_faces`.
        - Inside `reference_faces`, create subdirectories for each person, with the subdirectory name being the person's name.
        - Add reference images to the corresponding subdirectory.
    - Create a directory named `test_faces`.
        - Add test images to this directory.

## Usage

1. **Running the Script:**
    ```bash
    python face_recognition.py
    ```

    - The script will load the reference and test images, perform face recognition, and print the best match for each test face image.

## Example Usage
**Here is an example output:**
```bash
Best match for test1.jpg: person1
Best match for test2.jpg: person2
Person not present in the reference dataset: test3.jpg
```

## Project Overview

### Load Reference Face Images

The script loads reference face images from the `reference_faces` directory, with subdirectories for each person. It encodes these images for face recognition.

### Load Test Face Images

Test face images are loaded from the `test_faces` directory. Each test face is encoded and compared to the reference faces to find the best match.

### Face Recognition

The script uses the `face_recognition` library to calculate the distances between the test face encoding and the reference face encodings. It identifies the best match based on the smallest distance, provided it is below a specified threshold.


