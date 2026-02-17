import cv2 as cv
import mediapipe as mp
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


#path
model_path = "../model/hand_landmarker.task"


#task
BaseOptions = mp.tasks.BaseOptions(model_asset_path=model_path)
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult # result
result_container = None

def print_result(result: HandLandmarkerResult, output_image:mp.Image, timestamp_ms: int) :
    # print('Hand landmarker result : {}'.format(result))
    global result_container
    result_container = result

options = HandLandmarkerOptions(
    base_options=BaseOptions,
    running_mode=VisionRunningMode.LIVE_STREAM, 
    result_callback=print_result,
    num_hands=2
)


#camera
cap = cv.VideoCapture(0)
#camera loop
with HandLandmarker.create_from_options(options) as landmarker :
    while cap.isOpened() :
        ret, frame = cap.read()
        
        if not ret : 
            break
    
        rgb_image_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        mp_image_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image_frame)

        
        # logic
        frame_timestamp_ms = int(time.time() * 1000)
        landmarker.detect_async(mp_image_frame, frame_timestamp_ms)
        
        if result_container is not None :
            if result_container.hand_landmarks :
                for hand_landmarks in result_container.hand_landmarks :

                    height, width, _ = frame.shape

                    for landmark in hand_landmarks :
                        pixel_x = int(landmark.x * width)
                        pixel_y = int(landmark.y * height)
                        cv.circle(frame, (pixel_x, pixel_y), 5, (255, 0, 0), -1   )
        
        cv.imshow('tab', frame)

        
        if cv.waitKey(1) == ord('q') :
            break

cap.release()
cv.destroyAllWindows()