from tkinter import *

root = Tk()

root.geometry("733x434")
root.minsize(300, 300)
root.maxsize(800, 800)

# Adding a label to the GUI window
shark = Label(text="Hey! How you doin'?")
shark.pack()    # Need to pack the components in order to display them

root.mainloop()
