class Student:
    def __init__(self,sid,dept):
        self.sid=sid
        self.dept=dept

class Faculty:
    def __init__(self,eid,dept):
        self.eid=eid
        self.dept=dept
class PhdStudent(Student, Faculty):
    def __init__(self,id,dept):
        super().__init__(id,dept)
ps=PhdStudent(123,'CSE')
print(ps.sid)
print(ps.dept)

#The Diamond problem

class Person:
    def __init__(self,id,n):
        self.id=id
        self.name=n
class Student(Person):
    def __init__(self,id,n):
        super().__init__(id,n)
    def PrintDetails(self):
        print("Student:")
        print(self.id,self.name)
class Faculty(Person):
    def __init__(self,id,n):
        super().__init__(id,n)
    def PrintDetails(self):
        print("Faculty:")
        print(self.id,self.name)
class PhdStudent(Student, Faculty):
    def __init__(self,id,n):
        super().__init__(id,n)
ps=PhdStudent(123,'abc')
ps.PrintDetails()