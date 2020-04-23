#coding=utf-8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "点击"
        self.btn01.pack()
        self.btn01["command"] = self.textCall  # 创建退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def textCall(self):
        messagebox.showinfo("love","I love you")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+200")
    root.title("")
    app = Application(master=root)
    root.mainloop()