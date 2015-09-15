class Car:
    def __init__(self):
        self.color = 'White'
        self.km_per_liter = 15
    def __str__(self):
        return 'Car:->Color:' + self.color+'->Km/l:' + str(self.km_per_liter)
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return  self.color
    def set_km_per_liter(self,kpl):
        self.km_per_liter = kpl
    def get_km_per_liter(self):
        return self.km_per_liter

class Hybrid(Car):
    def __init__(self):
        Car.__init__(self)
        self.battery_life=20
    def __str__(self):
        s=Car.__str__(self)
        s = s+'->Battery Life:'+str(self.battery_life)
        return s
    def set_battery_life(self,bl=20):
        self.battery_life=bl
    def get_battery_life(self):
        return self.battery_life

c = Car()
h = Hybrid()
h.set_color('Red')
print(c)
print(h)

