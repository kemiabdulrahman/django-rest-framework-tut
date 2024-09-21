import math

from .shape import Shape

class Rectangle(Shape):
    
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    
    def describe(self):
        parent_description = super().describe()
        return f"{parent_description} It is a rectangle with a width of {self.width} and an height of {self.height}"
    
    