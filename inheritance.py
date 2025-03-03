class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname, subject,marks):
        super().__init__(fname,lname)
        self.academ=[(subject,marks)]

    def add_few(self,subject,marks):
      self.academ.append((subject,marks))

    def printall(self):
      for subject,marks in self.academ:
             print(f"{subject}:{marks}")
p1=Student("soukya","jain","maths",22)
p1.add_few("science",24)
p1.printname()
p1.printall()


