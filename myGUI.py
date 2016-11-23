# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox
#导入Tkinter包中的所有内容

class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
	#	self.helloLabel = Label(self,text = 'Hello,world')
	#	self.helloLabel.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.helloButton = Button(self,text = 'Hello',command = self.hello)
		self.helloButton.pack()
		self.quitButton = Button(self,text = 'Quit',command = self.quit)
		self.quitButton.pack()


	def hello(self):
		name = self.nameInput.get() or 'World'
		messagebox.showinfo('Message','Hello,%s' % name)


#实例化Application

app = Application()
#设置窗口标题

app.master.title('Hello My world!')

app.mainloop()

