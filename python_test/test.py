class MyRectangle:

    def __init__(self,x = 0,y = 0,width = 100,height = 100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        S = self.width*self.height
        print("矩形面积等于{0}".format(S))

    def getPerimeter(self):
        C = 2*(self.height+self.width)

        print("矩形周长等于{0}".format(C))

    def draw(self):
        import turtle
        t = turtle.Pen()
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.goto(self.x+self.width,self.y)
        t.goto(self.x+self.width,self.y+self.height)
        t.goto(self.x,self.y+self.height)
        t.goto(self.x,self.y)
        turtle.done()
rect = MyRectangle()
rect.getArea()
rect.getPerimeter()
rect.draw()