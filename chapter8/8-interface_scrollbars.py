from Tkinter import *

window = Tk()

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill= Y)

listbox = Listbox(window)
listbox.pack()

for i in range(20):
    listbox.insert(END,i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

window.mainloop()
