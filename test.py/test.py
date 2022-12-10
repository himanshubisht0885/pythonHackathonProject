from tkinter import *
from tkinter import ttk


root=Tk()
root.title("test")
mainframe=ttk.Frame(root,padding="3 3 12 12")
button=ttk.Button(root,text='hello',command='buttonpressed')
button.grid()
root.mainloop()