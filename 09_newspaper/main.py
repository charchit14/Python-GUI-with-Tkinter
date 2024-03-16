# Sample Newspaper Design

from tkinter import *

root = Tk()

root.geometry("1080x720")

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




# # Third Image (Bottom Left)
# img3 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\jessP.png")
# img3_label = Label (image=img3)
# img3_label.pack(side=BOTTOM, anchor=W)

# # Description for the third image
# text3 = Label(text='''The woman in this picture is Jess Park.
#               She plays for Manchester City.
#               She is a Forwarder.
#               She represents England at national level''',
#               bg="black", fg="skyblue", font=50)
# text3.pack(side=BOTTOM, anchor=W)


# # Fourth Image (Bottom Right)
# img4 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\yuiH.png")
# img4_label = Label (image=img4)
# img4_label.pack(side= BOTTOM, anchor=E)

# # Description for the second image
# text4 = Label(text='''The woman in this picture is Yui Hasegawa.
#               She plays for Manchester City.
#               She is a Mid-fielder.
#               She represents Japan at national level''',
#               bg="black", fg="yellow", font=50)
# text4.pack(side=BOTTOM, anchor=E)


root.mainloop()
