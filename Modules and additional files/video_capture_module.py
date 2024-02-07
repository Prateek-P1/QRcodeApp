import cv2
def video_capture():
    cam=cv2.VideoCapture(0)
    return cam

def waiter_key():
    key_code=cv2.waitKey(50)
    return key_code