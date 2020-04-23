#coding=utf-8
from tkinter import *


class Application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWeiget()
    def createWeiget(self):
        self.label01 = Label(self,text="用户名")
        self.label01.grid(row=0, column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0,column=1)
        self.label02 =Label(self,text="密码")
        self.label02.grid(row=1, column=0)
        self.entry02 = Entry(self,show="*")
        self.entry02.grid(row=1, column=1)
        self.btn01 = Button(self, text="登录")
        self.btn01.grid(row=2, column=1, sticky=EW)
        self.btn02 = Button(self, text="注册")
        self.btn02.grid(row=3, column=1)

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+100+100")
    app = Application(master=root)
    root.mainloop()