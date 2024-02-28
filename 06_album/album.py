from tkinter import *

root = Tk()

# Inserting the text
text_label = Label(text="This is my album")
text_label.pack()

# Inserting images
img = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\06_album\images\photo-01.png")
img_label = Label(image=img)
img_label.pack()


root.mainloop()
