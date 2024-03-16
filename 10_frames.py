from tkinter import *
root = Tk()

root.geometry("720x640")

# Creating a frame
f1 = Frame(root, bg="pink", borderwidth=6, relief=RAISED)   # 'root' indicates that the frame is to be placed inside the root
f1.pack(side=LEFT, fill="y")

# Creating a label to place in the frame
t1 = Label(f1, text="I'm inside a frame", font="80")
t1.pack(pady=200)


# Crating second frame
f2 = Frame(root, bg="yellow", borderwidth=8, relief=GROOVE)
f2.pack(side=TOP, fill="x")

# Creating a label for second frame
t2 = Label(f2, text="WELCOME TO MY WORLD",font="100", fg="red")
t2.pack(pady=100)

root.mainloop()
