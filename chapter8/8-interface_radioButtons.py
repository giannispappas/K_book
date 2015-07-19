from Tkinter import *

def radiofunction1():
    print('1η επιλογή')
def radiofunction2():
    print('2η επιλογή')
def radiofunction3():
    print('3η επιλογή')

window = Tk()
rbfr = Frame(window)
rbfr.pack(side = TOP, fill = X)
Label(rbfr, text='Επιλογές:').pack(side=LEFT)
basis = IntVar()
r1 = Radiobutton(rbfr, text ='1η επιλογή', value=1, variable=basis, command=radiofunction1())
r1.pack(side=LEFT)
r2 = Radiobutton(rbfr, text ='2η επιλογή', value=2, variable=basis, command=radiofunction2())
r2.pack(side=LEFT)
r3 = Radiobutton(rbfr, text ='3η επιλογή', value=3, variable=basis, command=radiofunction3())
r3.pack(side=LEFT)
r1.select()
window.mainloop()
