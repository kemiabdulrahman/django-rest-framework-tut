import math

from .shape import Shape

class Circle(Shape):
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    
    def describe(self):
        parent_description = super().describe()
        return f"{parent_description} It is a circle with a radius of {self.radius}"
    
    