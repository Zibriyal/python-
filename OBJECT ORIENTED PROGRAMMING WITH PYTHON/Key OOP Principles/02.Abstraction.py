"""Abstraction is a core concept in Object-Oriented Programming (OOP) that involves hiding complex implementation details and only exposing the necessary functionality. It allows developers to define what something does without specifying how it does it, making the code cleaner, promoting reusability, and reducing complexity.

Abstraction with a Shape Class
Imagine you're developing a graphics software where different shapes need to be drawn and manipulated. To make the code reusable, you decide to create a base class called Shape. This class will contain properties that all shapes share, such as:

Color
Name
Boundary Style (e.g., dotted or solid lines)
And more...
Additionally, every shape will need certain methods like draw() and getArea(), but the specific details of how these methods should be implemented for different shapes are not known at this level. For example, the getArea() method for a Rectangle will differ from that of a Circle.

To implement this, we use abstraction by defining Shape as an abstract class. Here’s how it looks in Python:"""

from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

# Concrete class Rectangle
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

    def get_area(self, length, breadth):
        return length * breadth

# Concrete class Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

    def get_area(self, radius):
        return 3.14159 * radius * radius