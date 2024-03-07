from tkinter import *
root = Tk()

root.geometry("720x440")

my_label = Label(text="Hi! Lechal",
                 bg="pink", fg="red",
                 font="44", borderwidth=6, relief=RAISED)

# Using different pack options
my_label.pack(side=BOTTOM, anchor="se", # 'se' means SouthEast
              fill=X,   # This will fill the X-axis, as we increase the window size, X-axis will be automatically filled by this label
              padx=60, pady=10)   

# To fill on the Y-axis; we need to change the side to either 'LEFT' or 'RIGHT'

root.mainloop()


# Important Pack Options
# anchor    :   N, W, S, E (Direction towards which the label should be packed (North, West, South, East))
# side      :   top, bottom, left, side (Side towards which the label should be packed (By default, it is 'top'))
# fill      :   Fill a particular axis(X or Y) with the label
# padx      :   X-padding
# pady      :   Y-padding
