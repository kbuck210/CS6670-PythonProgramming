## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/14/14

## All Cores Frame

from tkinter import *
from bargraphframe import *

class AllCoresFrame(Frame):
    # default blank list class variable
    cores = []
    
    def __init__(self,base,n):
        Frame.__init__(self,base,bd=1,relief="groove")
        for i in range(0,n):
            AllCoresFrame.cores.append(BarGraphFrame(self, "Core {}".format(i+1), scale=.65))
            AllCoresFrame.cores[i].grid(row=0,column=i,sticky='w,e,n,s')

    # Method to setup each canvas in the frame
    def setupCanvases(self):
        for core in AllCoresFrame.cores:
            core.setupCanvas()

    # Method called by the controller to update each core with psutil data
    def updateCores(self, corelist):
        for i, core_data in enumerate(corelist):
            AllCoresFrame.cores[i].setPercent(core_data)
