from tkinter import *

def resize(ev = None):
    label.config(font = 'Helvetica -%d bold'%scale.get())

top =Tk()
top.geometry('700x500')

label = Label(top,text = 'Hello world',font= 'Helvetica -18 bold')
label.pack(fill = Y,expand = 1)

scale = Scale(top,from_ = 10, to = 80,orient = HORIZONTAL,command = resize)
scale.set(18)
scale.pack(fill = X,expand = 1)

quit = Button(top,text = 'Quit',command = top.quit,activeforeground = 'white',activebackground = 'red')
quit.pack()

mainloop()











