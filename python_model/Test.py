#coding=utf-8
from tkinter import *


root = Tk()
root.geometry("500x300")
c1 = Canvas(root,width=100,height=100,bg="blue")
c1.pack()
c2 = Button(root, text="测试")
c2.pack()
def mouseTest(event):
    print("父容器点击位置{0},{1}".format(event.x,event.y))
    print("子容器点击位置{0},{1}".format(event.x_root, event.y_root))
    print("绑定组件{0}".format(event.widget))
def keyboard(event):
    print(" press a")
def keyboardTest(event):
    print("键盘按键{0},{1},{2}".format(event.char,event.keycode,event.keysym))
def mouseTest01(a,b):
    print("a={0},b={1}".format(a,b))
def mouseTest02(event):
    print("绑定类")
    print(event.widget)

c1.bind("<Button-1>",mouseTest)
root.bind("<KeyPress-a>",keyboard)
root.bind("<KeyPress>",keyboardTest)
Button(root, text="测试lambda", command=lambda: mouseTest01("mys","24")).pack()
c2.bind_class("Button","<Button-3>",mouseTest02)
root.mainloop()