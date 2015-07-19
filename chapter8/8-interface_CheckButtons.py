from Tkinter import *

window = Tk()

cbfr = Frame(window)
cbfr.pack(side=TOP)
var = IntVar()
c = Checkbutton(cbfr, text='Επιλογή', state=NORMAL, variable=var)
c.pack(side=LEFT)

window.mainloop()
