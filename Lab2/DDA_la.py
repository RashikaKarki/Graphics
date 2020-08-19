from graphics import *
import time

def DDA_line(x1, y1, x2, y2):

    # creating the window
    winX = 600
    winY = 600
    win = GraphWin('DDA Line', winX, winY)

    # measure the distance
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # measuring the steps
    if (dx > dy):
        steps = dx
    else:
        steps = dy

    xinc = dx/steps
    yinc = dy/steps

    # loop for making the line based on point
    x = x1
    y = y1
    for i in range(steps+1): 
        PutPixle(win,x,y)
        x += xinc
        y += yinc         
        time.sleep(0.01)
        print(x,y)       


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

    DDA_line(x1, y1, x2, y2)


if __name__ == "__main__":
    main()