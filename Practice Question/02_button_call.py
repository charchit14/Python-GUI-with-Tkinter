# Question: WAP to create four buttons and print sth different each time they are called (Stack the buttons horizontally)

from tkinter import *
root = Tk()

root.geometry("480x320")
root.title("The Buttons Call")


# Defining the functions
def name():
    print("Name: Shark")

def profession():
    print("Profession: Jobless")

def hobby():
    print("Hobby: Crying")

def extra():
    print("Extra: No")


# Creating frame
f1 = Frame(root, bg="pink", borderwidth=4, relief=RAISED)
f1.pack(side=TOP, anchor="nw")


# Creating the buttons
b1 = Button(f1, text="Name", command=name)
b1.pack(side=LEFT, padx=6)

b2 = Button(f1, text="Profession", command=profession)
b2.pack(side=LEFT, padx=6)

b3 = Button(f1, text="Hobby", command=hobby)
b3.pack(side=LEFT, padx=6)

b4 = Button(f1, text="Extra", command=extra)
b4.pack(side=LEFT, padx=6)


# Creating a Label
l = Label(text="Look at your IDE's terminal", fg="red", font=18, pady=20)
l.pack()


root.mainloop()
