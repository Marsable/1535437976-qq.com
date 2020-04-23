#coding=utf-8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWeiget()

    def createWeiget(self):
        # 用户框

        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")


        # 密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        Button(self, text="登陆", command=self.login).pack()
    def login(self):
        print("yhm:"+ self.entry01.get())
        print("mm:" + self.entry02.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+100+100")
    app = Application(master=root)

    root.mainloop()
