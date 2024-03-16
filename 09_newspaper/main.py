# Sample Newspaper Design

from tkinter import *

root = Tk()

root.geometry("1920x1080")

root.title("The Guardian")

# Newspaper Title
# Title Frame
header_frame = Frame(root, bg="black", borderwidth=4)
header_frame.pack(side=TOP)

# Title Description
header_title = Label(header_frame, text=''' The Guardian
                 \n March 9, 2024
                 \n Manchester, England''', font="Courier 14 bold")
header_title.pack()


# First News
# News Frame
f1 = Frame(root, bg="yellow", borderwidth=6)
f1.pack(side=LEFT, fill=Y)

# News Photo 
i1 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\alexG.png")
i1_label = Label(f1, image=i1)
i1_label.pack()

# News Description
t1 = Label(f1, text=''' The woman in this picture is Alex Greenwood.
               \nShe plays for Manchester City.
               \nHer position is Center-Back.
               \nShe represents England at national level.''',
               bg="black", fg="skyblue", font=50)
t1.pack(pady=25)


# Second News
# News Frame
f2 = Frame(root, bg="pink", borderwidth=6)
f2.pack(side=RIGHT, fill=Y)

# News Photo 
i2 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\chloeK.png")
i2_label = Label(f2, image=i2)
i2_label.pack()

# News Description
t2 = Label(f2, text='''The woman in this picture is Chloe Kelly.
               \nShe plays for Manchester City.
               \nShe is a Forwarder.
               \nShe scored the winning goal for England at Euro24. ''',
               bg="black", fg="skyblue", font=50)
t2.pack(pady=25)


# Third News
# News Frame
f3 = Frame(root, bg="grey", borderwidth=6)
f3.pack(side=TOP, fill=X)

# News Photo
i3 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\jessP.png")
i3_label = Label(f3, image=i3)
i3_label.pack()

# News Description
t3 = Label(f3, text=''' The woman in this picture is Jess Park.
                \nShe plays for Manchester City.
                \nShe is a Forwarder.
                \nShe represents England at national level. ''',
                bg="black", fg="skyblue", font=50)
t3.pack(pady=25)


# Fourth News
# News Frame
f4 = Frame(root, bg="green", borderwidth=6)
f4.pack(side=BOTTOM, fill=X)

# News Photo
# i4 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\yuiH.png")
i4 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\logo.png")
i4_label = Label(f4, image=i4)
i4_label.pack()

# News Description
t4 = Label(f4, text=''' The woman in this picture is Yui Hasegawa.
                \nShe plays for Manchester City.
                \nShe is a Mid-fielder.
                \nShe represents Japan at national level. ''',
                bg="black", fg="skyblue", font=50)
t4.pack(pady=25)


root.mainloop()
