from tkinter import *
import os

root = Tk()

# Inserting the text
text_label = Label(text="This is my album")
text_label.pack()


# Creating a frame to hold the images (Optional)
# frame = Frame(root)
# frame.pack()


# Defining the images path
path = r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\06_album\images"


# Creating a list to hold all the images
img_list = []

# Adding all the images to the list
for i in os.listdir(path):
    if i.endswith(".png"):
        img_list.append(i)


# Inserting the images in the GUI window
for j in img_list:
    img = PhotoImage(file=os.path.join(path,j))
    # img_label = Label(frame, image=img)
    img_label = Label(root, image=img)
    img_label.image = img
    img_label.pack(side=LEFT)

root.mainloop()
