from graphics import *
from time import sleep
from math import sqrt,sin,cos, pi
from sympy import symbols, Eq, solve
from Arc import Arc

win = GraphWin('Face', 500, 500)

def drawmoon():
    #Drawing moon 
    arc = Arc(Point(210, 190), Point(245, 220), -180)
    arc.setOutline('white')
    arc.setFill('white')
    arc.draw(win)

    #Drawing waves from moon
    r1 = 8
    r2 = 12
    cx = 227
    cy = 205

    triangle_vertices = []
    degree = 0
    for i in range(25):
        if ((i+1) % 2 ) != 0:
            angle = degree * ( pi / 180 )
            x = int(cx + r1 * cos(angle))
            y = int(cy + r1 * sin(angle))
        else:
            angle = degree * ( pi / 180 )
            x = int(cx + r2 * cos(angle))
            y = int(cy + r2 * sin(angle))

        degree = degree + 15
        triangle_vertices.append(Point(x,y))

        if (len(triangle_vertices) % 3 ) == 0:
            triangle = Polygon(triangle_vertices)
            triangle.setFill('white')
            triangle.setOutline('white')
            triangle.draw(win)
            triangle_vertices= [triangle_vertices[2]]

    circle = Circle(Point(227, 205), 8)
    circle.setFill('white')
    circle.setOutline('white')
    circle.draw(win)

def drawsun():
    #Drawing Sun
    r1 = 10
    r2 = 18
    cx = 230
    cy = 270
    #main circle
    circle = Circle(Point(230, 270), r1)
    circle.setFill('white')
    circle.setOutline('white')
    circle.draw(win)

    triangle_vertices = []
    degree = 0
    for i in range(25):
        if ((i+1) % 2 ) != 0:
            angle = degree * ( pi / 180 )
            x = int(cx + r1 * cos(angle))
            y = int(cy + r1 * sin(angle))
        else:
            angle = degree * ( pi / 180 )
            x = int(cx + r2 * cos(angle))
            y = int(cy + r2 * sin(angle))

        degree = degree + 15
        triangle_vertices.append(Point(x,y))

        if (len(triangle_vertices) % 3 ) == 0:
            triangle = Polygon(triangle_vertices)
            triangle.setFill('white')
            triangle.setOutline('white')
            triangle.draw(win)
            triangle_vertices= [triangle_vertices[2]]


def main():
    #Measurements
    left_bot = Point(200, 300)
    right_bot = Point(300, 300)
    left_top = Point(200, 167)

    #Finding plots for left mid
    x, y = symbols('x y')
    eq1 = Eq(600*x + 600*y - 170000 - (x**2) - (y**2))
    eq2 = Eq(-x + y)
    solution = solve((eq1,eq2), (x, y))
    left_mid = Point(solution[0][0],300 - (solution[1][0]-300))

    right_mid = Point(300,300 - (solution[1][0]-300))

    #coloring the triangles
    #botton triangle
    triangle = Polygon([left_bot, right_bot, Point(200 , 200)])
    triangle.setFill('red')
    triangle.setOutline('red')
    triangle.draw(win)
    #upper triangle
    triangle = Polygon([left_top, right_mid, Point(200 , 300 - (solution[1][0]-300))])
    triangle.setFill('red')
    triangle.setOutline('red')
    triangle.draw(win)

    #Drawing the base line
    line = Line(left_bot,right_bot)
    line.setOutline('blue')
    line.setWidth(3)
    line.draw(win)
    #Drawing the verticle line
    line_verticle = Line(left_top, left_bot)
    line_verticle.setOutline('blue')
    line_verticle.setWidth(3)
    line_verticle.draw(win)
    #Drawing the bottom triangle
    line_bot_triangle = Line(right_bot,left_mid)
    line_bot_triangle.setOutline('blue')
    line_bot_triangle.setWidth(3)
    line_bot_triangle.draw(win)
    #Drawing Middle line
    line_middle = Line(left_mid, right_mid)
    line_middle.setOutline('blue')
    line_middle.setWidth(3)
    line_middle.draw(win)
    #Drawing the upper triangle
    line_up_triangle = Line(left_top,right_mid)
    line_up_triangle.setOutline('blue')
    line_up_triangle.setWidth(3)
    line_up_triangle.draw(win)

    drawmoon()

    drawsun() 

    #For closing the graphics window
    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

