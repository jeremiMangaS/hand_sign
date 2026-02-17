import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open the camera")
    exit()
while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        print("Can't receive frame (stream end?), Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # print(f"Width : {cap.get(cv.CAP_PROP_FRAME_WIDTH)} \nHeight : {cap.get(cv.CAP_PROP_FRAME_HEIGHT)}")

    cv.imshow('frame', gray)
    cv.moveWindow('frame', 250, 250)
    if cv.waitKey(1) == ord('q') : 
        break

cap.release()
cv.destroyAllWindows()

