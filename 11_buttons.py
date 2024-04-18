from tkinter import *
root = Tk()

root.geometry("720x480")
root.title("Buttons")

f1 = Frame(root, bg="yellow", borderwidth=4, relief=GROOVE)
f1.pack(side=TOP)

b1 = Button(f1, fg="pink", text="This is the button")
b1.pack()



root.mainloop()
