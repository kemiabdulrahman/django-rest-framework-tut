from mypackage.circle import Circle
from mypackage.rectangle import Rectangle as rec


def main():
    
    shapes = [
        Circle("red", 3),
        rec("blue", 3, 4)
    ]
    
    for shape in shapes:
        print(shape.describe())
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
        
        
if __name__ == "__main__":
    main()