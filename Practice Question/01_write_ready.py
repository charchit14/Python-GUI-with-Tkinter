# Question: Make a 500 x 400 window and write 'READY' at the bottom of the window

from tkinter import *

root = Tk()

root.geometry("500x400")

my_text = Label(text="READY", bg="pink", fg="red", font=100)

my_text.pack(side=BOTTOM, fill=X)

root.mainloop()
