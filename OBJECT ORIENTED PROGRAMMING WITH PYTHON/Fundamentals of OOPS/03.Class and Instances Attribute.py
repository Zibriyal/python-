class Employee:
    compName='gfg'
    def __init__(self,id):
        self.id=id

e=Employee(1001)
print(e.compName)
print(e.id)
print(Employee.compName)

class Employee:
    compName='gfg'
    def __init__(self,id):
        self.id=id
e1=Employee(1001)
e2=Employee(1002)
Employee.compName='geeksforgeeks'
print(e1.compName)
print(e2.compName)


class Employee:
    compName='gfg'
    def __init__(self,id):
        self.id=id
    def fun(self,n):
        self.name=n
e=Employee(1001)
e.fun('abhi')
print(e.name)
e.designation='CEO'
print(e.designation)
Employee.officeAddress='Noida'
print(Employee.officeAddress)
print(e.officeAddress)

print('--------------------------------------------------')

class Employee:
    compName='gfg'
    def __init__(self,id):
        self.id=id
e=Employee(1001)
Employee.officeAddress='Noida'
e.officeAddress='NCR'
print(Employee.officeAddress)
print(e.officeAddress)