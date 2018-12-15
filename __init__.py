from tkinter import*
import os
import sys    
class Maker:
    def __init__(self):
        self.master = Tk()
        self.master.title('AppMaker')
    def run(self):
        self.master.mainloop()
    def SetBtn(self, text = None , command = None, row = None , col = None):
        self.text = text
        self.command = command
        self.row = row
        self.col = col
        Button(self.master, text=self.text, command = self.command).grid(row = self.row, column = self.col)
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
    def SetText(self,text, row = None , col = None, fg = 'black', bg = None):
        self.text = text
        self.row = row
        self.col = col
        self.fg = fg
        self.bg = bg
        Label(self.master,text=self.text,fg=self.fg,bg=self.bg).grid(row=self.row,column=self.col)
    def SetEntryBox(self,row = None,col=None):
        self.row = row
        self.col = col
        self.e = Entry(self.master).grid(row = self.row, column=self.col)