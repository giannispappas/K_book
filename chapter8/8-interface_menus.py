from Tkinter import *

def testing():
    print("Just testing!")

window = Tk()
window.title('Python book')
menu = Menu(window)
window.config(menu=menu)
yearmenu = Menu(menu)
menu.add_cascade(label='Year', menu=yearmenu)
yearmenu.add_command(label='2014', command=testing)
yearmenu.add_command(label='2015', command=testing)
yearmenu.add_separator()
yearmenu.add_command(label='Exit', command=testing)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=testing)
mainloop()
