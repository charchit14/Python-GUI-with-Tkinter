from tkinter import *

root = Tk()

text_label = Label(text="This is my album")
text_label.pack()



img = PhotoImage(file="images\\photo-01.png")
# img = PhotoImage(file="C:\Users\charc\Desktop\Python\Python GUI with Tkinter\06_album\images\photo-01.png")
img_label = Label(image=img)
img_label.pack()


root.mainloop()
