# -*- coding: utf-8 -*- 
from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text='hello world')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='quit',command = self.quit)
        self.quitButton.pack()
app = Application()
app.master.title('Hello World')
app.mainloop()
#tkinter是python的标准库，记住首先初始化一个大窗口，即init方法，然后再初始化布局
#每创建一个组件，需要用self.pack()进行打包，负责显示
#最后对图形界面进行实例化，设定标题等等

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)
app = Application()
app.master.title('Hello World')
app.mainloop()
#实际上UI编程，可以在widget当中的command变量中定义执行的程序
#先画UI，再执行方法程序
