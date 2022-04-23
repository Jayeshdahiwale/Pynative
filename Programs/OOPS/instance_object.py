"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Python program to create a Vehicle class with max_speed and mileage instance attributes.

"""

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
if __name__ == "__main__":
    modelX = Vehicle(240, 18)
    print(modelX.max_speed, modelX.mileage)