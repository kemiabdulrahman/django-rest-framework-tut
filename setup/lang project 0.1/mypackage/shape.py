from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self, color):
        self.color = color
        
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
        
    @abstractmethod
    def describe(self):
        return f"This is a {self.color} shape"
    
