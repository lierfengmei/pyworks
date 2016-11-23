
from tkinter import *
import tkinter.messagebox


class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='欢迎使用应答器教学仿真系统！')
        self.helloLabel.pack()
        self.baliseButton = Button(self,text='模拟BTM',command = self.baliseWidgets)
        self.baliseButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command = self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self,text='Quit',command = self.quit)
        self.quitButton.pack()

    def baliseWidgets(self):
        self.baliseLabel = Label(self,text = "This is the Balise param")
        self.baliseLabel.pack()

    def hello(self):
        name = self.nameInput.get() or 'lifengmei'
        tkinter.messagebox.showinfo('Message','hello, %s'%name)


app = Application()
app.master.title('应答器教学仿真系统!')
app.mainloop()

