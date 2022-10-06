# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:46:00 2022

@author: PC_RC
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Image Opener")
root.geometry("500x500")
root.configure(background = "lightgrey")

label_image = Label(root, bg="white", highlightthickness = 2)
label_image.place(relx = 0.5, rely = 0.4, anchor = CENTER)

img_name = ""

def openimage():
    global img_name
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes=(("Image Files", "*.jpg;*.gif;*.png;*.jpeg"),))
    print(img_path)
    img_e = ImageTk.PhotoImage(Image.open(img_path))
    label_image['image'] = img_e
    img_path.close()
    
btn_open = Button(root, text = "Open Image", font = ("algerian", 9, "bold"), bg = "lightgrey", fg = "black", relief= "solid", padx = 5, pady = 5, command = openimage)
btn_open.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()

    
   
       