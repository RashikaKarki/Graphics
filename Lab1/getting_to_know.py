import graphics
from graphics import Text, Point

#Creating a window
win = graphics.GraphWin()

#Printing window size
print("The window is of pixel ",win.getHeight(), "X",win.getWidth()) #By default it is 200X200

#Creating graphic window of pixel 500X500
win = graphics.GraphWin('Lab 1', 500, 500)

#For closing the graphics window
message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
message.draw(win)
win.getMouse()
win.close()