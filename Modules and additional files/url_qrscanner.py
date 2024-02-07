import cv2
import numpy as np
import video_capture_module as VC
import quit_program_module as QP
import qr_read as QR
import qrscan_display as QSCAN

def qrcode_scanner():

    def decoder(image):                                   #USER DEFINED FUNCTION TO PROCESS AND DECODE THE QRCODE
        gray_img = QR.qrcode_reader(image,0)
        barcode = QR.qrcode_decoder(gray_img)
        flag=0
        while flag!=1:
            for obj in barcode:
                points = obj.polygon                         #MAKING A POLIGON USING THE VERTICES TO READ QRCODE IN DIFFERENT ORIENTATIONS
                (x, y, w, h) = obj.rect
                pts = np.array(points, np.int32)             #ARRAY OF POINTS(USING NUMPY MODULE)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                barcodeData = obj.data.decode("utf-8") #DEFAULT ENCODING USED IS UTF-8
                barcodeType = obj.type
                if barcodeData != False:
                    string= QSCAN.qrdata(barcodeData,barcodeType)

                    cv2.putText(frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    QSCAN.qrdisplay(barcodeData,barcodeType)
                    flag=1
                exit()
            flag=1

    cap = VC.video_capture()                         #TO CAPTURE REAL TIME VIDEO FROM WEBCAM
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('QRScanner', frame)        #TO DISPLAY THE REAL TIME VIDEO IN A WINDOW
        code = VC.waiter_key()                        #WAITS 10ms
        if QP.quit_program(code)=='T':                          #PRESSING Q TO EXIT THE SCANNER
            break