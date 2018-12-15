from tkinter import*
import os
import sys    
class Maker:
    def __init__(self):
        self.master = Tk()
        self.master.title('AppMaker')
    def run(self):
        self.master.mainloop()
    def SetCaption(self,caption = 'AppMaker'):
        self.caption = caption
        self.master.title(self.caption)
    def SetSize(self,size):
        self.size = size
        self.master.geometry(self.size)
    def SetMinSize(self,width, height):
        self.width = width
        self.height = height
        self.master.minsize(width = self.width , height=self.height)
    def SetMaxSize(self,width, height):
        self.width = width
        self.height = height
        self.master.maxsize(width = self.width , height=self.height)
    def SetConfigure(self,bgcolor):
        self.bgcolor = bgcolor
        self.master.configure(bg = self.bgcolor)
class SetBtn:
    def __init__(self, master, text=None , command = None , row = None , col= None):
        self.master = master
        self.text = text
        self.command = command
        self.row = row
        self.col = col
        Button(self.master,text=self.text,command=self.command).grid(row=self.row,column=self.col)
app = Maker()
b1 = SetBtn(app.master, 'text')
app.run()
