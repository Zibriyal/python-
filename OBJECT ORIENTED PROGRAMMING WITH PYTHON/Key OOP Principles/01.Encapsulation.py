"""Consider a scenario where you are a new employee tasked with designing a Date class for your company's library.
Initially, you might store the date as a string:"""

class Date:
    def __init__(self, date_str):
        self.val = date_str

    def get(self):
        return self.val

"""Every team in your company uses this Date class. Later, you realize that storing the date as a string is not efficient and decide to change the internal representation to three integer members: dd, mm, and yyyy.

However, since the val member was not hidden, other programmers might have directly accessed it using d.val. Changing the internal representation now breaks their code."""

"""The Importance of Encapsulation
Encapsulation allows you to hide the internal representation of data members. By providing methods like get and avoiding direct access to data members, you can change the internal structure without affecting the external code.

For example, after encapsulation, you can modify the get method to return a string composed of the three integer members:"""

class Date:
    def __init__(self, dd, mm, yyyy):
        self.__dd = dd
        self.__mm = mm
        self.__yyyy = yyyy

    def get(self):
        return f"{self.__dd}/{self.__mm}/{self.__yyyy}"


"""Enhancing Maintainability and Consistency
Encapsulation not only improves maintainability but also ensures consistency across your codebase. By restricting access to data members, you can enforce rules and validations in one place.

Example: Student Class with Private Fields
Consider a Student class with a marks field that should only hold values between 0 and 100. Without encapsulation, other classes could directly modify marks, leading to invalid values.

By making marks private and providing a setter method, you can enforce these constraints:"""

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100")

    def get_marks(self):
        return self.__marks

"""This approach ensures that marks are always within the valid range, maintaining consistency throughout the application."""