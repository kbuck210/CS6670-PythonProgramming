## CS672 - Python Programming - Hackathon
## Kevin C. Buckley
## 11/13/14

## Bar Graph Frame for CPU/Mem usage

from tkinter import *

class BarGraphFrame(Frame):

    def __init__(self, base, label,scale=1):
        self.hFrame = 200*scale
        self.wFrame = 100*scale
        self.hCanvas = 200*scale*(.75)
        self.wCanvas = 100*scale*(.75)
        Frame.__init__(self, base, height=self.hFrame, width=self.wFrame, bd=0, relief="groove")                   
        self.percent = 0
        self.canvas = Canvas(self, bd=1, height=self.hCanvas, width=self.wCanvas, relief="ridge", bg="black")
        self.canvas.grid(row=0, padx=10, pady=0, sticky='w,e,n,s')
        self.title = Label(self, text=label, bd=0, relief="ridge").grid(row=1, pady=0, sticky='n')
        
    def setupCanvas(self):
        self.canWidth = self.canvas.winfo_width()
        self.canHeight = self.canvas.winfo_height()
        self.pad = self.canWidth * (.10)
        self.x1 = self.pad
        self.y2 = self.canHeight - self.pad
        self.x2 = self.canWidth - self.pad
        self.y1 = self.y2 - ((self.canHeight - (2*self.pad)) * (self.percent/100))
        self.canvas.create_rectangle(self.x1, self.x1, self.x2, self.y2, fill="black", outline="green3")
        self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="green2", outline="green3")
        
    def setPercent(self,p):
        self.percent = p
        self.setupCanvas()
        
