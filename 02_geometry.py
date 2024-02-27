from tkinter import *

# Creating base class
root = Tk()

# To alter the size of the GUI window (width x height)
root.geometry("400x500")

# Minimum size of the GUI window (width, height) (We can't shrink the window beyond these dimesnisons)
root.minsize(250, 300)

# Maximum size of the GUI window (width, height) (We can't increase the window beyond these dimesnisons)
root.maxsize(800, 800)

root.mainloop()
