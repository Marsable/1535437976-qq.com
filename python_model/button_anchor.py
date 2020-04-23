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
        self.btn01 = Button(root, text="登陆", command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file ="imgs/start.gif")
        self.btn02 = Button(root, image=photo, command=self.login)#加()返回的是一个值，不加返回的才是方法
        self.btn02.config(state="disabled")
        self.btn02.pack()

    def login(self):
        messagebox.showinfo("btn","这是btn测试")


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+100+100")
    app = Application(master=root)
    root.mainloop()