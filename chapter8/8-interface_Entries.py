from Tkinter import *

window = Tk()
e = Entry(window)
e.pack()
e.focus_set()

def getFunction():
    t=e.get()
    print(t)
def insertFunction():
    e.delete(0,10)
    print(e.insert(0,'Hello'))
def clearFunction():
    e.delete(0,10)

b1 = Button(window,text='Εισαγωγή', width=10, command=getFunction)
b1.pack()
b2 = Button(window,text='Εμφάνιση', width=10, command=insertFunction)
b2.pack()
b3 = Button(window,text='Καθαρισμός', width=10, command=clearFunction)
b3.pack()

window.mainloop()

