from Tkinter import *

window = Tk()

Label(window, text='Κείμενο -1:').grid(row=0, sticky=W)
Label(window, text='Κείμενο -2:').grid(row=1, sticky=W)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

cb = Checkbutton(window, text = 'Επιλογή')
cb.grid(row=2, columnspan=2, sticky=W)

window.mainloop()

