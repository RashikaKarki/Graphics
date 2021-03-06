from graphics import *
import time
import math

def scale(x,y):
    winX = 800
    winY = 800
    win = GraphWin('Scaling', winX, winY)
    x1, y1 = 150, 150
    x2,y2 = 250,150
    x3,y3 = 300,200
    a = PutPixle(win,x1, y1)
    b = PutPixle(win,x2,y2)
    c = PutPixle(win,x2,y2)
    d = PutPixle(win,x3,y3)
    e = PutPixle(win,x1,y1)
    ab = PutLine(win,"red",a,b)
    bc = PutLine(win,"red",b,c)
    cd = PutLine(win,"red",c,d)
    de = PutLine(win,"red",d,e)
    ea = PutLine(win,"red",e,a)
    x1, y1 = 150*x, 150*y
    x2,y2 = 250*x,150*y
    x3,y3 = 300*x,200*y
    a = PutPixle(win,x1, y1)
    b = PutPixle(win,x2,y2)
    c = PutPixle(win,x2,y2)
    d = PutPixle(win,x3,y3)
    e = PutPixle(win,x1,y1)
    ab = PutLine(win,"blue",a,b)
    bc = PutLine(win,"blue",b,c)
    cd = PutLine(win,"blue",c,d)
    de = PutLine(win,"blue",d,e)
    ea = PutLine(win,"blue",e,a)
    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    pt.draw(win)
    return pt

def PutLine(win, color, point1, point2):
    """ Plot A Pixle In The Windows At Point (x, y) """
    line = Line(point1, point2)
    line.setOutline(color)
    print(color)
    line.draw(win)

def main():
    x = input("enter x the scaling factor")
    y = input("enter y the scaling factor")
    scale(int(x),int(y))

if __name__ == "__main__":
    main()