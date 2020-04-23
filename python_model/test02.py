# coding=utf-8
from tkinter import *
from tkinter import messagebox

root = Tk()  # 根窗口
root.title("test01")
root.geometry("300x200+100+200")
btn01 = Button(root)
btn01["text"] = "text"

btn01.pack()


def text(e):  # 事件对象
    messagebox.showinfo("Message", "亲亲我吧")
    print("etxtsa")


btn01.bind("<Button-1>", text)
root.mainloop()
# 必须调用的mainloop方法,检测用户事件，激活窗口
