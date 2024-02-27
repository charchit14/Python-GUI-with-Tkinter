from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("720x612")

# Inserting text
my_text = Label(text="Red Bird")
my_text.pack()

# Inserting 'jpg' images
img_path = Image.open("bird.jpg")
img = ImageTk.PhotoImage(img_path)
img_label = Label(image=img)
img_label.pack()

root.mainloop()
