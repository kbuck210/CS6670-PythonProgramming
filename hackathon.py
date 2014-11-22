##
## Controller
##

##  Lessons Learned:
##
##  1. Tkinter formatting, configuring rows/cols for equal spacing, gridlayout
##  2. 

from time import sleep
import baseview, psutildata
from usagedb import UsageDB

class Controller():
    # The data model is a dictionary of values read from psutil
    model = dict()
    cpu_buff = []   #
    mem_buff = []   # Buffers to store data to only write to DB once a min
    net_buff = []   #
    dsk_buff = []   #
    usr_buff = []   #
    prc_buff = []   #
        
    def __init__(self):
        # Establish the database connection via an instance of UsageDB class
        Controller.db = UsageDB("usage.sqlite")
    
        # Establish the data model dictionary
        self.updateModel()
        self.view = baseview.View(self)
        self.view.setUpdateInterval(1000)
        # Get the number of cores found in psutil & update gui
        self.view.setCores(len(Controller.model['cpu'][1]))
        self.db.updateCpuCols(len(Controller.model['cpu'][1]))
        self.view.startGui()

    # Call the method to update the GUI with the current model information
    def updateGui(self):
        self.updateModel()
        self.view.updateTotCpuPct(Controller.model['cpu'][0])
        self.view.updateCoreGraphs(Controller.model['cpu'][1])
        self.view.updateTotMemPct(Controller.model['mem'].percent)
        self.view.updateInfoPanel('mem', Controller.model['mem'])
        self.view.updateInfoPanel('dsk', Controller.model['dsk'])
        self.view.updateInfoPanel('usr', Controller.model['usr'])
        self.view.updateInfoPanel('net', Controller.model['net'])
        self.view.updateProcCount(Controller.model['prc'])

    # Update the local data model based on data read from psutil,
    # adding each reading to the buffer
    def updateModel(self):
        Controller.model['cpu'] = psutildata.getCpuData()
        Controller.cpu_buff.append(Controller.model['cpu'])
        Controller.model['mem'] = psutildata.getMemData()
        Controller.mem_buff.append(Controller.model['mem'])
        Controller.model['net'] = psutildata.getNetData()
        Controller.net_buff.append(Controller.model['net'])
        Controller.model['usr'] = psutildata.getUserInfo()
        Controller.usr_buff.append(Controller.model['usr'])
        Controller.model['dsk'] = psutildata.getDiskData()
        Controller.dsk_buff.append(Controller.model['dsk'])
        Controller.model['prc'] = psutildata.getProcCount()
        Controller.prc_buff.append(Controller.model['prc'])

        # Check the buffer lengths, if length = 60 (1 minutes data),
        # clear buffers & write to DB
        if len(Controller.prc_buff) > 59:
            self.writeToDB()

    # Call the methods to write out the local model to the database
    def writeToDB(self):
        # Clear each buffer by copying to new list for writing, & reassigning
        cb = Controller.cpu_buff
        mb = Controller.mem_buff
        nb = Controller.net_buff
        sb = Controller.dsk_buff
        ub = Controller.usr_buff
        pb = Controller.prc_buff

        Controller.cpu_buff = [] #
        Controller.mem_buff = [] # Reassign lists so that they're clear
        Controller.net_buff = [] # by the next read on the model
        Controller.dsk_buff = [] #
        Controller.usr_buff = [] #
        Controller.prc_buff = [] #

        self.view.setStatusWorking()
        Controller.db.insertCpuData(cb)
        Controller.db.insertMemData(mb)
        Controller.db.insertNetData(nb)
        Controller.db.insertDskData(sb)
        Controller.db.insertUsrData(ub)
        Controller.db.insertPrcData(pb)
        self.view.setStatusReady()

        
##############################
## Main:
## 1. Start the web-services to get/create database
## 2. Get an instance of the controller, creating a local data model & view
## 3. Give a handle to the database for the web-server class
## 4. Controller updates local data model & view, uses handle to call web
##      services to update database
## 5. Web service can access existing database & view results
if __name__ == "__main__":
    x = Controller()
    
