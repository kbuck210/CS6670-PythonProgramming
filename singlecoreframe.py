##
##
##

## Single Core Frame

from tkinter import *

class SingleCoreFrame(Frame):

    def __init__(self, base, h, w, n):
        Frame.__init__(self,base, height=h, width=w)
        self.canvas = Canvas(self, bd=1, relief="ridge", bg="black", height=h*(.8) width=w*(.8))
        self.canvas.grid(row=0, padx=2, pady=2, sticky='w,e,n,s')
        self.title = Label(self, text="Core {num}".format(num=n))
        self.title.grid(row=1, sticky='n')
