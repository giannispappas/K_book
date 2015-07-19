from Tkinter import *

class Application:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.qbutton = Button(frame, text = 'Quit', fg = 'red', command=frame.quit)
        self.qbutton.pack(side=LEFT)
        self.mbutton = Button(frame,text='Message', command = self.print_message)
        self.mbutton.pack(side=LEFT)
    def print_message(self):
        print('Hello World!')

root = Tk()
app = Application(root)
root.mainloop()
