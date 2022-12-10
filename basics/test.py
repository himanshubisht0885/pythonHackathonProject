from tkinter import *
from tkinter import ttk


root=Tk()
root.title("test")
#creating a label widget 
mylabel1=Label(root,text='hello world')
mylabel2=Label(root,text='hello world12133')
mylabel3=Label(root,text='                  ')
#shoving it onto the screen // can you .pack() or .grid()
mylabel1.grid(row=0,column=0)
mylabel3.grid(row=1,column=1)
mylabel2.grid(row=1,column=5)
mainframe=ttk.Frame(root,padding="3 3 12 12")


#creating buttons
mybutton=Button(root,text='click me',padx=50,pady=50) #add state=DISABLED  # padding x axis padx
mybutton.grid(row=3,column=6)
root.mainloop()