# Q2: Newspaper (images and text, newspaper title, date, ...)

from tkinter import *

root = Tk()

root.title("The Guardian")


# Newspaper Description
news_des = Label(text='''The Guardian
                \n March 9, 2024
                \n Manchester, England''', font="comicsansm 14 bold")
news_des.pack()





# First Image (Top Left)
img1 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\alexG.png")
img1_label = Label(image=img1)
img1_label.pack(side=TOP, anchor=W)
# img1_label.grid(row=0, column=0, sticky=W)

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

# Third Image (Bottom Left)
img3 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\jessP.png")
img3_label = Label (image=img3)
img3_label.pack(side=BOTTOM, anchor=W)

# Fourth Image (Bottom Right)
img4 = PhotoImage(file=r"C:\Users\charc\Desktop\Python\Python GUI with Tkinter\09_newspaper\images\yuiH.png")
img4_label = Label (image=img4)
img4_label.pack(side= BOTTOM, anchor=E)





root.mainloop()