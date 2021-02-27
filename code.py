import cv2
import os

cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    #capture frame-by-frame
    ret, frames = video_capture.read()

    cv2.imshow('Camera', frames)

    #press 'q' in 20 miliseconds to exit
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()