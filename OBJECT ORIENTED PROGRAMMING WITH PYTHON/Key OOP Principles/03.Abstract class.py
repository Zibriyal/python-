"""Abstract classes allow you to define methods that must be created within any child classes built from the abstract class."""


from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def printSides(self):
        pass

class Triangle(Polygon):
    def __init__(self, color):
        super().__init__(color)

    def printSides(self):
        print("There are 3 sides")

b = Triangle("Red")
b.printSides()