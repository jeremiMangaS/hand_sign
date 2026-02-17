#import
import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#path
model_path = "model/hand_landmarker.task"
photo_path = "photo/image.jpg"


# task
BaseOptions = mp.tasks.BaseOptions(model_asset_path=model_path) # model path
HandLandmarker = mp.tasks.vision.HandLandmarker # to detect the landmark 
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions # to configure mediapipe handlandmarker task
VisionRunningMode = mp.tasks.vision.RunningMode # to configure the running mode of mediapipe program

options = HandLandmarkerOptions(
    base_options=BaseOptions,
    running_mode=VisionRunningMode.IMAGE)

image = cv.imread(photo_path)
rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

# logic
with HandLandmarker.create_from_options(options) as landmarker :
    hand_landmarker_result = landmarker.detect(mp_image)

    if hand_landmarker_result.hand_landmarks : # hand checking
        for hand_landmarks in hand_landmarker_result.hand_landmarks :
            
            height, width, _ = image.shape

            for landmark in hand_landmarks :
                # coordinates based on photo size
                pixel_x = int(landmark.x * width)
                pixel_y = int(landmark.y * height)
                cv.circle(image, (pixel_x, pixel_y), 5, (255, 0, 0), -1) # draw the points


    print(hand_landmarker_result)
    # 
    cv.imshow('tab', image)
    cv.waitKey(0)
    cv.destroyAllWindows()         