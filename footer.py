## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/14/14

## Footer Panel

from tkinter import *


class Footer(Frame):

    def __init__(self,base):
        Frame.__init__(self,base, height=1)
        self.pCount = 0
        self.cPer = 0
        self.mPer = 0
        # Define 3 frames to store ProcessCount, CPU usage %, and Memory Usage%
        self.proc = Label(self, text="Processes: {}".format(self.pCount), bd=1, relief='groove')
        self.cusg = Label(self, text="CPU Usage %: {}".format(self.cPer), bd=1, relief='groove')
        self.musg = Label(self, text="Mem Usage %: {}".format(self.mPer), bd=1, relief='groove')
        self.proc.grid(row=0,column=0,sticky='wens')
        self.cusg.grid(row=0,column=1,sticky='wens')
        self.musg.grid(row=0,column=2,sticky='wens')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

    def updateProc(self,p):
        self.pCount=p
        self.proc["text"]="Processes: {}".format(self.pCount)
            
    def updateCpu(self,c):
       self.cPer=c
       self.cusg["text"]="CPU Usage %: {}".format(self.cPer)
       
    def updateMem(self,m):
       self.mPer=m
       self.musg["text"]="Mem Usage %: {}".format(self.mPer)
