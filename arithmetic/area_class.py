class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
        
obj1=Rectangle(10,20)
print("Length =",obj1.length)
print("Breadth =",obj1.breadth)
print("Area of Rectangle =",obj1.area())
