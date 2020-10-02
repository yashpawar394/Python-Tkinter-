
from tkinter import *
#save to GitHub
root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

Label(root, text="First Name").pack()
Label(root, text="How many Siblings?").pack()

name = Entry(root)
SibNum = Entry(root)

root.mainloop()
