import cv2
import face_recognition
import os

# Load the reference face images
reference_faces_dir = 'reference_faces'
reference_faces = []
reference_face_names = []

for foldername in os.listdir(reference_faces_dir):
    folder_path = os.path.join(reference_faces_dir, foldername)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        img = face_recognition.load_image_file(os.path.join(folder_path, filename))
        reference_faces.append(face_recognition.face_encodings(img)[0])
        reference_face_names.append(foldername)

# Load the test face images
test_faces_dir = 'test_faces'

for filename in os.listdir(test_faces_dir):
    img = face_recognition.load_image_file(os.path.join(test_faces_dir, filename))
    test_face_encoding = face_recognition.face_encodings(img)[0]

    # Find the best match
    distances = face_recognition.face_distance(reference_faces, test_face_encoding)
    best_match_index = distances.argmin()

    # Check if the minimum distance is below a certain threshold (e.g., 0.6)
    if distances[best_match_index] < 0.6:
        print(f"Best match for {filename}: {reference_face_names[best_match_index]}")
    else:
        print(f"Person not present in the reference dataset: {filename}")