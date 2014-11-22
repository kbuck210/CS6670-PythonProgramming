## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/13/14

## Quad Info Panel

from tkinter import *
from singleinfopanel import *

class InfoPanel(Frame):

    info = dict()

    def __init__(self,base):
        Frame.__init__(self,base)
        InfoPanel.info['mem']=[['Total:',''],['Available:',''],['Used:',''],['Free:','']]
        InfoPanel.info['dsk']=[['Total:',''],['Free:',''],['Used:',''],['%:','']]
        InfoPanel.info['usr']=[['Name:',''],['Terminal:',''],['Host:',''],['Started:','']]
        InfoPanel.info['net']=[['Sent:',''],['Recieved:',''],['Drops-In:',''],['Drops-Out:','']]
        # Create Panels for Memory, Disk Space, Users, and Network
        self.mem = SingleInfoPanel(self,"Phsyical Memory: (MB)",InfoPanel.info['mem'])
        self.dis = SingleInfoPanel(self,"Disk Usage: (MB)",InfoPanel.info['dsk'])
        self.usr = SingleInfoPanel(self,"Root User Info:",InfoPanel.info['usr'])
        self.net = SingleInfoPanel(self,"Network Status (packets):",InfoPanel.info['net'])
        # Setup 4x4 grid
        self.mem.grid(row=0,column=0,sticky='n,w,e,s')
        self.dis.grid(row=1,column=0,sticky='n,w,e,s')
        self.net.grid(row=0,column=1,sticky='n,w,e,s')
        self.usr.grid(row=1,column=1,sticky='n,w,e,s')
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)


    def updateInfoPanel(self, key, newvals):
        if(key == 'mem'):
            InfoPanel.info['mem'][0][1] = '%.2f' % float(newvals.total/1000000)
            InfoPanel.info['mem'][1][1] = '%.2f' % float(newvals.available/1000000)
            InfoPanel.info['mem'][2][1] = '%.2f' % float(newvals.used/1000000)
            InfoPanel.info['mem'][3][1] = '%.2f' % float(newvals.free/1000000)
            self.mem.updateValues(InfoPanel.info['mem'])
        elif (key == 'dsk'):
            InfoPanel.info['dsk'][0][1] = '%.2f' % float(newvals.total/1000000)
            InfoPanel.info['dsk'][1][1] = '%.2f' % float(newvals.free/1000000)
            InfoPanel.info['dsk'][2][1] = '%.2f' % float(newvals.used/1000000)
            InfoPanel.info['dsk'][3][1] = newvals.percent
            self.dis.updateValues(InfoPanel.info['dsk'])
        elif (key == 'usr'):
            InfoPanel.info['usr'][0][1] = newvals.name
            InfoPanel.info['usr'][1][1] = newvals.terminal
            InfoPanel.info['usr'][2][1] = newvals.host
            InfoPanel.info['usr'][3][1] = newvals.started
            self.usr.updateValues(InfoPanel.info['usr'])
        elif (key == 'net'):
            InfoPanel.info['net'][0][1] = newvals[0]
            InfoPanel.info['net'][1][1] = newvals[1]
            InfoPanel.info['net'][2][1] = newvals[2]
            InfoPanel.info['net'][3][1] = newvals[3]
            self.net.updateValues(InfoPanel.info['net'])
        else:
            pass
            
