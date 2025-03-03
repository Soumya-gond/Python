class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("hello my name is "+ self.name +"and I'm " + str(self.age)  + "years old")

p1=person("soumya",22)
p1.myfunc()