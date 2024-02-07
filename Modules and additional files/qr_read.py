import cv2
from pyzbar.pyzbar import decode
def qrcode_reader(image,c):
    gray_img = cv2.cvtColor(image, c)  #c NEEDS TO BE 0
    return gray_img

def qrcode_decoder(gray_img):
    qrbarcode = decode(gray_img)
    return qrbarcode