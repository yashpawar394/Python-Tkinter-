from tkinter import *
#save to GitHub
root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

Label(root, text="First Name").grid(row=0)
Label(root, text="How many Siblings?").grid(row=1)

name = Entry(root)
SibNum = Entry(root)
