from tkinter import *
root = Tk()

root.geometry("720x480")
root.title("Buttons")

# Whenever a 'command' is used with name 'buttonClicked', this function gets called and the corresponding statement is printed on terminal
def buttonClicked():
    print("The button is working")


# Creating a frame
f1 = Frame(root, bg="yellow", borderwidth=4, relief=GROOVE)
f1.pack(side=TOP)

# Creating button inside a frame
b1 = Button(f1, fg="pink", text="This is the button", command=buttonClicked)    # 'command' will call the function named 'buttonClicked' (Just give the name of the function)
b1.pack(side=TOP, pady=5)

b2 = Button(f1, fg="pink", text="This is the button")
b2.pack(side=BOTTOM, pady=5)

b3 = Button(f1, fg="pink", text="This is the button")
b3.pack(side=LEFT, padx=5)

b4 = Button(f1, fg="pink", text="This is the button")
b4.pack(side=RIGHT, padx=5)


root.mainloop()
