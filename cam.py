import cv2
def cam_feed():
    vid = cv2.VideoCapture(0)
    while True:
        extra, frame= vid.read()
        yield frame





