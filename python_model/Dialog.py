# 文本框
#coding=utf-8

from tkinter import *
from tkinter.filedialog import *


filename=""

class Application(Frame):
    def __init__(self,master=None):
        super().__init__()

        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        #创建主菜单
        menubar = Menu(root)
        #创建下拉菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)
        #添加菜单名字
        menubar.add_cascade(label="文件", menu=menuFile)
        menubar.add_cascade(label="编辑", menu=menuEdit)
        menubar.add_cascade(label="帮助", menu=menuHelp)
        #添加菜单选项
        menuFile.add_command(label="新建" ,accelerator="ctrl+n" ,comman=self.newfile)
        menuFile.add_command(label="打开" ,accelerator="ctrl+o" ,comman=self.opnefile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", comman=self.savafile)
        menuFile.add_command(label="退出", accelerator="ctrl+q", comman=self.exitfile)
        root["menu"]=menubar

        self.textpad = Text(root,width=100,height=100)
        self.textpad.pack()
    def newfile(self):
        global filename
        root.title("未命名.txt")
        filename=None
        self.textpad.delete(1.0,END)
    def opnefile(self):
        global filename
        filename = askopenfilename(defaultextension=".txt")
        self.textpad.delete(1.0,END)
        with askopenfile(title="打开文本文件",defaultextension=".txt") as f:
            # print(f.name)
            self.textpad.insert(INSERT,f.read())
    def savafile(self):
        global filename
        with open(filename,"w") as f:
            c= self.textpad.get(1.0,END)
            f.write(c)
            f.close()

    def exitfile(self):
        root.quit()
if __name__ == '__main__':

    root=Tk()
    root.geometry("300x300")
    root.title("记事本")
    app = Application(master=root)
    root.mainloop()