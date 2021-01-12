from cam import cam_feed
import cv2
while True:
    try:
        print(cam_feed())
        for a in cam_feed():
            cv2.imshow('video',a)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exit()
    except Warning as e:
        print(e)


