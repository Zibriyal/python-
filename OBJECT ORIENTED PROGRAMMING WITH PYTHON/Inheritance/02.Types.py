#Multilevel Inheritance

class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def PrintDetails(self):
        print(self.id,self.name)

class Employee(Person):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary = salary

    def PrintDetails(self):
        super().PrintDetails()
        print(self.salary)
class SalesEmployee(Employee):
    def __init__(self,id,name,salary,si):
        super().__init__(id,name,salary)
        self.SalesInc = si
    def PrintDetails(self):
        super().PrintDetails()
        print(self.SalesInc)
se=SalesEmployee(123,"abc",40000,2000)
se.PrintDetails()
e=Employee(124,'xyz',50000)
e.PrintDetails()