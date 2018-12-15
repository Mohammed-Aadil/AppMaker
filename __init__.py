from tkinter import*
import os
import sys
def press():
    print('Working')
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
    def Caption(self,title = 'AppMaker'):
        self.title = title
        self.master.title(self.title)