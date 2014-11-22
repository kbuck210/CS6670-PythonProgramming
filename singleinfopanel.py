## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/13/14

## Description Panel

from tkinter import *

class SingleInfoPanel(Frame):
    
    # att parameter is a list of all of the attributes & their values
    def __init__(self,base,title,att):
        Frame.__init__(self,base, bd=1, relief="groove")
        self.title = Label(self, text=title)
        self.title.grid(row=0, columnspan=2,sticky='w,n,s')
        self.labels = []
        self.values = []
        for i,pair in enumerate(att):
            self.labels.append(Label(self,text=pair[0]))
            self.labels[i].grid(row=i+1,column=0,sticky='e,n,s')
            self.values.append(Label(self,text=str(pair[1])))
            self.values[i].grid(row=i+1,column=1,sticky='w,n,s')

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
    def updateValues(self,valuelist):
        for i, pair in enumerate(valuelist):
            self.values[i]["text"] = str(pair[1])
            
    
