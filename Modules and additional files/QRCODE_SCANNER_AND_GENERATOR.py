import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk
import help_module

import QR_GENERATE
import text_qrscanner
import url_qrscanner

# import png  # pip install pypng ## to save in png format
root = tk.Tk()

root.geometry("560x650")  # Size of the window
root.title("QRcode APP")  # Adding a title
root.iconbitmap('qr_app_icon.ico')     #Setting the icon image of the GUI window

my_notebook = ttk.Notebook(root)
my_notebook.grid(row=2, column=2)

my_frame1 = Frame(my_notebook, width=550, height=600)
my_frame2 = Frame(my_notebook, width=550, height=600)
my_frame3 = Frame(my_notebook, width=550, height=600)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="QRCODE GENERATOR")
my_notebook.add(my_frame2, text="TEXT SCANNER")
my_notebook.add(my_frame3, text="URL SCANNER")


def text_delete_function():
    e1.delete(1.0, END)


def clear_all_function():
    l1.config(image='')
    l1.image = None
    text_delete_function()

clear_icon=PhotoImage(file="clear_icon.png")

clear_button = tk.Button(my_frame1, font=16, text="Clear text", command=text_delete_function,image=clear_icon,compound=RIGHT)
clear_button.grid(row=1, column=1, padx=5, pady=10)


def on_enter(clear_button):
    clear_button.widget['background'] = 'orange'


def on_leave(clear_button):
    clear_button.widget['background'] = 'SystemButtonFace'

generate_icon=PhotoImage(file="generate_icon.png")

clear_button.bind('<Enter>', on_enter)
clear_button.bind('<Leave>', on_leave)

submit_button = tk.Button(my_frame1, font=16, text='Generate  ', command=lambda: QR_GENERATE.my_generate(e1, l1),
                          activeforeground="grey", activebackground="black",image=generate_icon,compound=RIGHT)
submit_button.grid(row=0, column=1, padx=5, pady=10)


def on_enter(submit_button):
    submit_button.widget['background'] = 'light green'


def on_leave(submit_button):
    submit_button.widget['background'] = 'SystemButtonFace'


submit_button.bind('<Enter>', on_enter)
submit_button.bind('<Leave>', on_leave)

refresh_icon=PhotoImage(file="refresh_icon.png")
refresh_button = tk.Button(my_frame1, font=16, text='Refresh  ', command=clear_all_function, activeforeground="grey",
                           activebackground="black",image=refresh_icon,compound=RIGHT)
refresh_button.grid(row=0, column=5)


def on_enter(refresh_button):
    refresh_button.widget['background'] = 'light blue'


def on_leave(refresh_button):
    refresh_button.widget['background'] = 'SystemButtonFace'


refresh_button.bind('<Enter>', on_enter)
refresh_button.bind('<Leave>', on_leave)

e1 = tk.Text(my_frame1, width=20, height=5, font=22, bg='lightblue', )
e1.grid(row=0, column=0, padx=10, pady=10)

l1 = tk.Label(my_frame1, text='QR to display here')
l1.grid(row=2, column=0, columnspan=2)


def text_launch_scanner():
    text_qrscanner.qrcode_scanner()

launch_icon=PhotoImage(file="launch_icon.png")

text_scanner_button = tk.Button(my_frame2, font=24, text="Launch Text Scanner", command=text_launch_scanner,image=launch_icon
                                ,compound=RIGHT)
(text_scanner_button
 .place(x=170, y=250))


def on_enter(text_scanner_button):
    text_scanner_button.widget['background'] = 'light blue'


def on_leave(text_scanner_button):
    text_scanner_button.widget['background'] = 'SystemButtonFace'


text_scanner_button.bind('<Enter>', on_enter)
text_scanner_button.bind('<Leave>', on_leave)


def url_launch_scanner():
    url_qrscanner.qrcode_scanner()


url_scanner_button = tk.Button(my_frame3, font=24, text="Launch URL Scanner", command=url_launch_scanner,image=launch_icon
                               ,compound=RIGHT)
url_scanner_button.place(x=170, y=250)


def on_enter(url_scanner_button):
    url_scanner_button.widget['background'] = 'light blue'

def on_leave(url_scanner_button):
    url_scanner_button.widget['background'] = 'SystemButtonFace'


url_scanner_button.bind('<Enter>', on_enter)
url_scanner_button.bind('<Leave>', on_leave)

help_icon=PhotoImage(file="question_mark_icon.png")
help_button = tk.Button(my_frame1, text="Help",font=16, command=lambda: help_module.help_function(),image=help_icon,compound=RIGHT)
help_button.grid(row=1,column=5)

url_note1=Label(my_frame3,font=8,text="Note: If a valid URL is found,it will automatically be opened on"
               ,fg="light blue")
url_note2=Label(my_frame3,font=8,text="the browser",fg="light blue")
url_note1.place(x=0,y=400)
url_note2.place(x=200,y=430)
def on_enter(help_button):
    help_button.widget['background'] = 'light blue'

def on_leave(help_button):
    help_button.widget['background'] = 'SystemButtonFace'


help_button.bind('<Enter>', on_enter)
help_button.bind('<Leave>', on_leave)

sv_ttk.set_theme("light")

root.mainloop()  # Keep the window open