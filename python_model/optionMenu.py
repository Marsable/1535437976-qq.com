# coding=utf-8
from tkinter import *

root=Tk()
root.geometry("300x300")


def text01(value):
    print("滑块",value)
    newFont = ("宋体" ,value)
    a.config(font=newFont)


s1 = Scale(root, from_=10 ,to = 50, length=200, tickinterval=5,orient=HORIZONTAL,command=text01)
s1.pack()
a = Label(root, text="猪")
a.pack()

root.mainloop()