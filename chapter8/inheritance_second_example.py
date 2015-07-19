class UniversityMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('->Αρχικοποίηση μέλους του Πανεπιστημίου:', self.name)
    def tell(self):
        print('Ονοματεπώνυμο:"{0}" Ηλικία:"{1}"'.format(self.name, self.age), end='')


class Professor(UniversityMember):
    def __init__(self, name, age, salary):
        UniversityMember.__init__(self,name,age)
        self.salary = salary
        print('->Αρικοποίηση καθηγητή:', self.name)
    def tell(self):
        UniversityMember.tell(self)
        print('Μισθός:', self.salary)


class Student(UniversityMember):
    def __init__(self,name, age, am):
        UniversityMember.__init__(self,name,age)
        self.am = am
        print('->Αρχικοποίηση φοιτητή:', self.name)
    def tell(self):
        UniversityMember.tell(self)
        print('ΑΜ:', self.am)


t = Professor('Αναστασίου Αναστάσιος', 45, 100)
s = Student('Αγγελίδης Αντώνιος', 20, 2075)

members = [t,s]
for member in members:
    member.tell()