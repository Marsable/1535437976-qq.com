from tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWeiget()
    def createWeiget(self):
        # self.photo = PhotoImage(file="imgs/puke/puke1.gif")
        # self.photo = PhotoImage(file="imgs/puke/puke2.gif")
        self.photos = [PhotoImage(file="imgs/puke/puke"+str(i+1)+".gif") for i in range(10)]
        self.pukes = [Label(root, image=self.photos[i])for i in range(10)]

        for i in range(10):
            self.pukes[i].place(x=10+i*40,y=50)
        print(self.pukes[1])
        self.pukes[0].bind_class("Label","<Button-1>",self.click)
    def click(self,event):
        if event.widget.winfo_y() ==50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x300+100+100")
    app = Application(master=root)
    root.mainloop()