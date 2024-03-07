from tkinter import *

root = Tk()

root.geometry("940x540")

# Changing the title that appears on the top bar of the GUI window
root.title("You see the change?")

# Some Label options
# text                  :   Add text
# font                  :   Change the font styling (Eg: font=("comicsansm", 36, "bold"))
# bd or background      :   Background
# fg or foreground      :   Foreground
# padx                  :   X-padding
# pady                  :   Y-padding
# relief                :   Border Styling (Types: SUNKEN, RAISED, GROOVE, RIDGE)

# Using different Label options
my_label = Label(text = '''This text has different effects.
                 \n You look beautiful in pink.''', 
                 bg="yellow", fg="red", font=("comicsansm", 36, "bold"))

my_label.pack()

root.mainloop()