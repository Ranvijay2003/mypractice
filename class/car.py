class Car:
    def __init__(self,model,year,engine,color):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        
    def __str__(self):
        return self.model + " " + str(self.year) + " " + self.engine + " " + self.color
        
my_car = Car('Toyota',2020,'V6','Red')
print("Car =", my_car)
print("Car Model =", my_car.model)
