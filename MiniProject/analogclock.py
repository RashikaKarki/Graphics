#This program creates an analog clock that keeps track of the current real world time.

from datetime import datetime
from math import pi, sin, cos
import tkinter


#Class for Clock
class AnalogClock:

    #Member Variables
    rootWindow = tkinter.Tk()
    canvas = tkinter.Canvas(rootWindow, width=600, height=600, borderwidth=0, highlightthickness=0, bg="white")
    time = datetime.now().time() #t.hour, t.min, t.sec
        
    #Updates the current time for the class object, so the TimeKeeper function can access it. 
    #Also deletes the previous lines for the hour, minute, and second hands
    def timeUpdate(self):
        self.canvas.delete("hour", "minute" , "second")
        self.time = datetime.now().time() #t.hour, t.min, t.sec
        self.TimeKeeper()
        self.rootWindow.after(500, self.timeUpdate)
    
    #Creates clock w/labels and labels the canvas
    def createCircleAndLabels(self):
        self.canvas.create_oval(100, 500, 500, 100, width = 2, fill='white')
        self.canvas.create_oval(295, 305, 305, 295, fill = "black")
        j = 0
        for i in range(0,60):
            angle = ((15-i)/15)*(pi/2.0)
            tipx = cos(angle) * 190
            tipy = sin(angle) * 190
            if i % 5 == 0:
                tipx = cos(angle) * 230
                tipy = sin(angle) * 230
                if j == 0:
                    self.canvas.create_text(300 + tipx, 300 - tipy, text = str(12), font = ("times new roman", 40))
                else:
                    self.canvas.create_text(300 + tipx, 300 - tipy, text = str(j), font = ("times new roman", 40))
                j = j + 1
            else:
                tipx = cos(angle) * 210
                tipy = sin(angle) * 210
                self.canvas
            
        
    #Calculates the angle for the new time, and draws the new lines for the hands
    def TimeKeeper(self):  
        timeSplit = str(self.time)
        timeSplit = timeSplit.split(":")
        iHr = int(timeSplit[0])
        iMin = int(timeSplit[1])
        iSec = round(float(timeSplit[2]))


        fHr = ((iHr % 12) * 5) + ((iMin/60) * 5)
        lenHourHand = 100
        fMin = ((iMin)) + ((iSec/60))
        lenMinuteAndSecHand = 150
        lenSecHand =  150
    
        #Draw Hour Hand
        angle = ((15-fHr)/15)*(pi/2.0)
        tipx = cos(angle) * lenHourHand
        tipy = sin(angle) * lenHourHand
        self.canvas.create_line(300, 300, 300 + tipx, 300 - tipy, width = 4, tags = "hour")

        #Draw Minute Hand
        angle = ((15-fMin)/15)*(pi/2.0)
        tipx = cos(angle) * lenMinuteAndSecHand
        tipy = sin(angle) * lenMinuteAndSecHand
        self.canvas.create_line(300, 300, 300 + tipx, 300 - tipy, width = 2, tags = "minute")


        #Draw Second Hand
        angle = ((15-iSec)/15)*(pi/2.0)
        tipx = cos(angle) * lenMinuteAndSecHand
        tipy = sin(angle) * lenMinuteAndSecHand
        self.canvas.create_line(300, 300, 300 + tipx, 300 - tipy, width = 2, fill = "black", tags = "second")
   
    #Packs the canvas, and recursively calls the timeUpdate function
    def end(self):
        self.canvas.pack()
        self.rootWindow.after(500, self.timeUpdate)
        self.rootWindow.mainloop()

def main():
    
    #Declare Object, and call its member functions
    MyClock = AnalogClock()
    MyClock.createCircleAndLabels()
    MyClock.TimeKeeper()
    MyClock.end()


if __name__ == "__main__":
    main()   