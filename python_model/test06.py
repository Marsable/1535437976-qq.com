# 文本选择框
# coding=utf-8

from tkinter import *
from  tkinter.filedialog import *

root=Tk()
root.geometry("300x300")


def textload():
    # f=askopenfilename(title="上传文件", initialdir="y:", filetype=[("图片文件","jpg")])
    f = askopenfile(title="打开文件",initialdir="y:", filetype=[("文本",".txt")])
    show["text"]=f.read()

Button(root, text="选择编辑的文件",command=textload).pack()
show=Label(root,width=10,height=3)
show.pack()
root.mainloop()