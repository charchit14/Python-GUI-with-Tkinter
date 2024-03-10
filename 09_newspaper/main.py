# Sample Newspaper Design

from tkinter import *

root = Tk()

root.geometry("1080x720")

root.title("The Guardian")


# Newspaper Description
news_des = Label(text='''The Guardian
                \n March 9, 2024
                \n Manchester, England''', font="Courier 14 bold")
news_des.pack()


# First Image (Top Left)
img1 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\alexG.png")
img1_label = Label(image=img1)
img1_label.pack(side=TOP, anchor=W)

# Description for the first image
text1 = Label(text='''The woman in this picture is Alex Greenwood.
              She plays for Manchester City.
              Her position is Center-Back.
              She represents England at national level.''',
              bg="black", fg="skyblue", font=50)
text1.pack(side=TOP, anchor=W)


# Second Image (Top Right)
img2 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\chloeK.png")
img2_label = Label (image=img2)
img2_label.pack(side=TOP, anchor=E)

# Description for the second image
text2 = Label(text='''The woman in this picture is Chloe Kelly.
              She plays for Manchester City.
              She is a Forwarder.
              She scored the winning goal for England at Euro24''',
              bg="black", fg="yellow", font=50)
text2.pack(side=TOP, anchor=E)


# Third Image (Bottom Left)
img3 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\jessP.png")
img3_label = Label (image=img3)
img3_label.pack(side=BOTTOM, anchor=W)

# Description for the third image
text3 = Label(text='''The woman in this picture is Jess Park.
              She plays for Manchester City.
              She is a Forwarder.
              She represents England at national level''',
              bg="black", fg="skyblue", font=50)
text3.pack(side=BOTTOM, anchor=W)


# Fourth Image (Bottom Right)
img4 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\yuiH.png")
img4_label = Label (image=img4)
img4_label.pack(side= BOTTOM, anchor=E)

# Description for the second image
text4 = Label(text='''The woman in this picture is Yui Hasegawa.
              She plays for Manchester City.
              She is a Mid-fielder.
              She represents Japan at national level''',
              bg="black", fg="yellow", font=50)
text4.pack(side=BOTTOM, anchor=E)


root.mainloop()
