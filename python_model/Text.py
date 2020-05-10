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
        self.w1 = Text(root, width=20, height=10, bg="gray")
        self.w1.pack()
        self.btn01 = Button()



if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+100+100")
    app = Application(master=root)

    root.mainloop()
