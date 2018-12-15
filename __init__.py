from tkinter import*
import os
import sys
def press():
    print('Working')
class Maker:
    def __init__(self, master = Tk()):
        self.master = master
        self.master.title('AppMaker')
    def run(self):
        self.master.mainloop()
class SetBtn:
    def __init__(self,master,text='',code = None,row = None, col = None):
        self.master = None
        self.text = text
        self.code = code
        self.row = row
        self.col = col
        Button(self.master, text=self.text,command=self.code).grid(row=self.row, column=self.col)
app = Maker()
b1 = SetBtn(app,'run',press)
app.run()
