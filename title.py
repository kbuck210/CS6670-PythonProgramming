## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/16/14

## Title Frame

from tkinter import *

class TitleBar(Frame):

    def __init__(self, base):
        Frame.__init__(self, base, height=2, bd=1, relief="groove")
        
        self.title = Label(self, text="System Health Monitor", padx=120)
        self.title.grid(row=0, sticky='w,e,n,s')
        
        self.status = Canvas(self,height=2,width=20, bd=1,relief="ridge",bg="green")
        self.status.grid(row=0,column=1,sticky='e,n,s')

    # Change the working indicator to red
    def setStatusWorking(self):
        self.status.config(bg="red")
        self.status.update_idletasks()

    # Change the working indicator to green
    def setStatusReady(self):
        self.status.config(bg="green")
        self.status.update_idletasks()
