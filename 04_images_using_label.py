from tkinter import *

root = Tk()

# Defining window size
root.geometry("640x380")

# Inserting text to our window 
text_label = Label(text="A beautiful view")
text_label.pack()

# Inserting image in our window
img = PhotoImage(file="tree.png")
image_label = Label(image=img)
image_label.pack()

root.mainloop()
