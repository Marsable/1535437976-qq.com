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

        self.Label01 = Label(self, text="Label", width=10, height=2, bg="green", fg="red", font=("宋体",15))

        self.Label01.pack()
        global photo #声明全局变量photo
        photo = PhotoImage(file="imgs/logo.gif")

        self.Label02 = Label(self, image=photo)
        self.Label02.pack()

        self.Label03 = Label(self,text="mys\nmarseer\n",
                             borderwidth=3, relief="groove", justify="right")
        self.Label03.pack()

        self.Label04 = Label(self,)

        #Options
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+200")
    root.title("Label")
    app = Application(master=root)
    root.mainloop()