from graphics import *
import time
import math

def Rotate(x):
    winX = 800
    winY = 800
    win = GraphWin('Rotation', winX, winY)
    x1, y1 = 350, 350
    x2, y2 = 350, 450
    a = PutPixle(win,x1, y1)
    b = PutPixle(win,x2,y2)
    ab = PutLine(win,"blue",a,b)
    x1 = math.floor(x1*math.cos(x) - y1*math.sin(x))
    y1 = math.floor(y1*math.cos(x) + x1*math.sin(x))
    x2 = math.floor(x2*math.cos(x) - y2*math.sin(x))
    y2 = math.floor(y2*math.cos(x) + x2*math.sin(x))
    print(x1,y1,x2,y2)
    print(math.cos(x),math.sin(x))
    a = PutPixle(win,x1, y1)
    b = PutPixle(win,x2,y2)
    ab = PutLine(win,"red",a,b)
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
    x = input("enter the rotation angle: ")
    angle = float(x)*(3.14/180)
    print(angle)
    Rotate(angle)

if __name__ == "__main__":
    main()

 
 
