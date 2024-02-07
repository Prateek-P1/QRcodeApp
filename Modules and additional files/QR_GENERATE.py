import pyqrcode
import tkinter as tk
def my_generate(e1,l1):
    global my_img
    my_qr = pyqrcode.create(e1.get(1.0,"end-1c"))

    my_qr.png("qrfoto.png", scale=6,
              module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
    my_qr = my_qr.xbm(scale=10)
    my_img = tk.BitmapImage(data=my_qr)
    l1.config(image=my_img)  # Show the qr code in Label