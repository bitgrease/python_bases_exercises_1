class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,d} miles"

    def drive(self, miles_driven):
        self.mileage += miles_driven

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)
new_car = Car("brown", 0)

print(blue_car)
print(red_car)
print(new_car)
print("Driving new car 100 miles.")
new_car.drive(100)
print(new_car)