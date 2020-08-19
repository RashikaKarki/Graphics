from graphics import *
import time

def MidPoint(X1,Y1,X2,Y2): 
    # creating the window
    winX = 600
    winY = 600
    win = GraphWin('Mid Point Line', winX, winY)

    # calculate dx & dy  
    dx = X2 - X1  
    dy = Y2 - Y1  
  
    # initial value of decision parameter d  
    d = dy - (dx/2)  
    x = X1 
    y = Y1  
  
    while (x < X2): 
        print(x,",",y,"\n") 
        PutPixle(win, x, y)
        x=x+1
        if(d < 0): 
            d = d + dy    
        else: 
            d = d + (dy - dx)  
            y=y+1

    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    pt.draw(win)

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp

    MidPoint(x1, y1, x2, y2)


if __name__ == "__main__":
    main()   
  

