class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def PrintDetails(self):
        print(self.id,self.name)

class SalesEmployee(Employee):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.SalesInc=salary

    def PrintDetails(self):
        super().PrintDetails()
        print(self.SalesInc)

el=[Employee(101,"zbc"),SalesEmployee(102,'bvc',5000)]

for e in el:
    e.PrintDetails()


print("-----------polymorphism in unrelated classes-----------------")


class Employee:
    def fun(self):
        print("Fun() of Employee")
class customer:

    def fun(self):
        print(" fun() ofCustomer")

l=[Employee(),customer()]
for e in l:
    e.fun()