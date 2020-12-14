from graphics import * 
import time
import math 
  
def translation(win, x, y):
    x1, y1 = 150 + x ,150 +y    
    x2,y2 = 150+ x ,250 +y     
    x3,y3 = 300+ x ,250+y 
    x4,y4 = 300+ x ,150 +y 
    x5, y5 = 150 + 100+ x , 150 + 70 +y     
    x6,y6 = 150+ 100+ x ,250+ 70  +y 
    x7,y7 = 300+ 100+ x ,250+ 70 +y 
    x8,y8 = 300+ 100+ x ,150 + 70 +y 

    a = PutPixle(win,x1, y1)     
    b = PutPixle(win,x2,y2)     
    c = PutPixle(win,x2,y2)     
    d = PutPixle(win,x3,y3)     
    e = PutPixle(win,x4,y4) 
    f = PutPixle(win,x5, y5)     
    g = PutPixle(win,x6,y6)     
    h = PutPixle(win,x6,y6)     
    i = PutPixle(win,x7,y7)     
    j = PutPixle(win,x8,y8) 

    ab = PutLine(win,"blue",a,b)     
    bc = PutLine(win,"blue",b,c)     
    cd = PutLine(win,"blue",c,d)     
    de = PutLine(win,"blue",d,e)     
    ea = PutLine(win,"blue",e,a) 
    fg = PutLine(win,"blue",f,g)     
    gh = PutLine(win,"blue",g,h)     
    hi = PutLine(win,"blue",h,i)     
    ij = PutLine(win,"blue",i,j)     
    jf = PutLine(win,"blue",j,f)  
    af = PutLine(win,"blue",a,f)     
    bg = PutLine(win,"blue",g,b)     
    di = PutLine(win,"blue",d,i)     
    ej = PutLine(win,"blue",e,j)


def cuboid(x,y): 
    winX = 800     
    winY = 800    
    win = GraphWin('Translation', winX, winY) 
 
    x1, y1 = 150, 150     
    x2,y2 = 150,250     
    x3,y3 = 300,250
    x4,y4 = 300,150 
    x5, y5 = 150 + 100, 150 + 70     
    x6,y6 = 150+ 100,250+ 70  
    x7,y7 = 300+ 100,250+ 70 
    x8,y8 = 300+ 100,150 + 70 

    a = PutPixle(win,x1, y1)     
    b = PutPixle(win,x2,y2)     
    c = PutPixle(win,x2,y2)     
    d = PutPixle(win,x3,y3)     
    e = PutPixle(win,x4,y4) 
    f = PutPixle(win,x5, y5)     
    g = PutPixle(win,x6,y6)     
    h = PutPixle(win,x6,y6)     
    i = PutPixle(win,x7,y7)     
    j = PutPixle(win,x8,y8) 

    ab = PutLine(win,"red",a,b)     
    bc = PutLine(win,"red",b,c)     
    cd = PutLine(win,"red",c,d)     
    de = PutLine(win,"red",d,e)     
    ea = PutLine(win,"red",e,a) 
    fg = PutLine(win,"red",f,g)     
    gh = PutLine(win,"red",g,h)     
    hi = PutLine(win,"red",h,i)     
    ij = PutLine(win,"red",i,j)     
    jf = PutLine(win,"red",j,f)  
    af = PutLine(win,"red",a,f)     
    bg = PutLine(win,"red",g,b)     
    di = PutLine(win,"red",d,i)     
    ej = PutLine(win,"red",e,j)


    ## Translation
    translation(win, x, y)

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
    line.draw(win) 
 
def main(): 
    x = input("enter x the translation factor")      
    y = input("enter y  the translation factor")  
    cuboid(int(x),int(y))


if __name__ == "__main__": 
         main() 