"""
Implements is-a raltionshp
code reusability
method overriding
abstract classes

"""
class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
class Employee(Person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary = salary

    def PrintDetails(self):
        print(self.id,self.name,self.salary)

e=Employee(123,"<NAME>",20000)
e.PrintDetails()
