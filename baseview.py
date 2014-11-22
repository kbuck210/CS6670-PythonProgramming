## CS672 - Python Programing Hackathon
## Kevin C. Buckley
## 11/13/14

## TKinter Viewer

from tkinter import *
from bargraphframe import *
from allcoresframe import *
from infopanel import *
from footer import *
from title import TitleBar

class View:
    cores = 4

    # Define constructor to launch TKinter view
    def __init__(self, controller):
        self.controller = controller
        self.baseView = Tk()
        self.baseView.title("Python Hackathon")
        #self.title = Label(self.baseView,height=2, text="System Health Monitor", bd=1, relief="groove")
        self.title = TitleBar(self.baseView)
        self.title.grid(row=0, columnspan=2, sticky='w,e,n,s')
        self.bars = Frame(self.baseView, bd=1,relief="groove")
        self.bars.grid(row=1,rowspan=2)
        self.cpu_graph = BarGraphFrame(self.bars, "CPU")
        self.mem_graph = BarGraphFrame(self.bars, "Mem")
        self.cpu_graph.grid(row=0, sticky='w,e,n,s')
        self.mem_graph.grid(row=1, sticky='w,e,n,s')
        self.all_cores = AllCoresFrame(self.baseView, View.cores)
        self.all_cores.grid(row=1,column=1, sticky='w,e,n,s')
        self.info = InfoPanel(self.baseView)
        self.info.grid(row=2,column=1, sticky='w,e,n,s')
        self.foot = Footer(self.baseView)
        self.foot.grid(row=3,columnspan=2,sticky='wens')
        #setup the bargraph canvases
        self.baseView.update_idletasks()
        self.cpu_graph.setupCanvas()
        self.mem_graph.setupCanvas()
        self.all_cores.setupCanvases()

    # Sets the number of cores from the data model, affecting the view
    def setCores(self,n):
        View.cores=n

    # Set the update interval (ms)
    def setUpdateInterval(self, ms):
        self.interval = ms

    # Calls the method to start the gui
    def startGui(self):
        self.updateGui()
        self.baseView.mainloop()

    # Defines the update method called every interval (ms) to update the gui
    def updateGui(self):
        self.baseView.after(self.interval, self.controller.updateGui)
        self.baseView.after(self.interval, self.updateGui)

    # Update the CPU Used percentage bar graph & footer with psutil data
    def updateTotCpuPct(self, pct):
        self.cpu_graph.setPercent(pct)
        self.foot.updateCpu(pct)

    # Update the Memory Used percentage bar graph & footer with psutil data 
    def updateTotMemPct(self, pct):
        self.mem_graph.setPercent(pct)
        self.foot.updateMem(pct)

    # Update each of the CPU core graphs
    def updateCoreGraphs(self, corelist):
        self.all_cores.updateCores(corelist)

    # Update the Info Panel for each of the Categories
    def updateInfoPanel(self, key, newvals):
        self.info.updateInfoPanel(key, newvals)

    # Update the footer with the count of total processes
    def updateProcCount(self, pids):
        self.foot.updateProc(pids)

    # Update the title status to working
    def setStatusWorking(self):
        self.title.setStatusWorking()

    # Update the title status to ready
    def setStatusReady(self):
        self.title.setStatusReady()
        
