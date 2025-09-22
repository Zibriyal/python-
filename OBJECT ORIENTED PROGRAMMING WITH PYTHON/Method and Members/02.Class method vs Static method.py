#Example to changes class attribute

class Employee:
    compName="gfg"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def setcompName(cls,cname):
        cls.compName=cname

Employee.setcompName("geeksforgeeks")
print(Employee.compName)
e=Employee("John",20)
print(e.compName)

print("-------------Create and instance------------------------------")

from datetime import date
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getFromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

e=Employee.getFromBirthYear("John",1982)
print(e.name)
print(e.age)


print("--------------static method examples-----------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        return (age >= 18)

    def PrintDetails(self):
        print(self.name)
        print(self.age)
        print(Person.isAdult(self.age))

P=Person("John",20)
P.PrintDetails()
print(Person.isAdult(24))
