from Tkinter import *

window = Tk()
textfr = Frame(window)
textfr.pack(side=TOP)
text = Text (textfr, height=5, width =10, font='Arial 24')
text.pack(side=LEFT)
text.insert(END,'Hello world!')
window.mainloop()
