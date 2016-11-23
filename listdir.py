import os
from time import sleep
from tkinter import *

class DirList(object):
    def __init__(self,initdir = None):
        self.top = Tk()
        self.label = Label(self.top,text = 'Directory Lister V1.1.1')
        self.label.pack()

        self.cwd = StringVar(self.top)

        self.dir = Label(self.top,fg='blue',font = ('Helvetica',12,'bold'))
        self.dir.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side = RIGHT,fill = Y)
        self.dirs = Listbox(self.dirfm,height = 15, width = 50, yscrollcommand = self.dirsb)


def main():
    d = DirList(os.curdir)
    mainloop()

if __name__=='__main__':
    main()