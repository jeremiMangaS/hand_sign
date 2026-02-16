import cv2 as cv
import mediapipe as mp
import numpy as np

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

img = cv.imread("image.jpg")

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

MARGIN = 10 #px
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) #vibran green

def draw_landmarks_on_image(rgb_image, detection_result) : 
    hand_landmark_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)
    #loop
    for indx in range(len(hand_landmark_list)) : 
        hand_landmark = hand_landmark_list[indx]
        handedness = handedness_list[indx]
        #draw hand landmarks
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmark,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )
        #detect hand bounding box
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmark]
        y_coordinates = [landmark.y for landmark in hand_landmark]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN
        #draw handedness on image
        cv.putText(annotated_image, f"{handedness[0].category_name}",
                   (text_x, text_y), cv.FONT_HERSHEY_DUPLEX,
                   FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv.LINE_AA)
        return annotated_image

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)
image = mp.Image.create_from_file("image.jpg")
detection_result = detector.detect(image)
annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
cv.imshow('test_image',cv.cvtColor(annotated_image, cv.COLOR_RGB2BGR))
cv.waitKey(0)