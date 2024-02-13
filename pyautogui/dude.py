from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
root.mainloop()