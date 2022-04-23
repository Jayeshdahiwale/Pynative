"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
a default value of 50.

"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    # assign default value to capacity

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())