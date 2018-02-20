"""
CS241 Checkpoint 07B
Written by Chad Macbeth
"""

"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        # This function calls the abstract method get_area 
        # The individual derived classes will provide an 
        # implementation for get_area.
        print("{} - {:.2f}".format(self.name, self.get_area()))

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
 
    def __init__(self):
        self.name = "Circle"
        self.radius = 0.0

    def get_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self):
        self.name = "Rectangle"
        self.length = 0.0
        self.width = 0.0

    def get_area(self):
        return self.length * self.width 

def main():

    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            c = Circle()
            c.radius = radius
            shapes.append(c)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            r = Rectangle()
            r.length = length
            r.width = width
            shapes.append(r)


    # Done entering shapes, now lets print them all out:

    for shape in shapes:
        shape.display()   # Polymorphism ... calling the abstract method and python will
                          # figure out which get_area to call

if __name__ == "__main__":
    main()

