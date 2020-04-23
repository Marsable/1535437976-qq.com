#coding=utf-8
from tkinter import *
from tkinter import messagebox
import random

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWeiget()

    def createWeiget(self):
        self.canvas = Canvas(self, width=200, height=200, bg="green")
        self.canvas.pack()
        line = self.canvas.create_line(10,20,30,30)
        rect = self.canvas.create_rectangle(50,50,100,100)
        circle = self.canvas.create_oval(50,50,100,100)
        self.btn01 = Button(self, text="点击创建矩形",command=self.drawRect)
        self.btn01.pack()
    def drawRect(self):
        for i in range(0,10):
            x1 = random.randrange(int(self.canvas["width"]))
            y1 = random.randrange(int(self.canvas["height"]))
            x2 = random.randrange(int(self.canvas["width"]))
            y2 = random.randrange(int(self.canvas["height"]))
            self.canvas.create_oval(x1,x2,y1,y2)

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+100+100")
    app = Application(master=root)
    root.mainloop()