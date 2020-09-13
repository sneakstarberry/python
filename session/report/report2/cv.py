import cv2

capture = cv2.VideoCapture('./movie.mp4')
while True:
    retval, frame = capture.read()
    if not retval:
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(30)
    if key == 27:
        break
if capture.isOpened():
    capture.release()
cv2.destroyAllWindows()