class FirstClass:
    def __init__(self,value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print 'Current value =', self.data
        
a = SecondClass(15)
a.display()
