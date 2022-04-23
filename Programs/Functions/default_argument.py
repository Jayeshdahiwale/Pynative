"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Giving default argument to function

"""
# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

if __name__ == "__main__":
    show_employee("Ben", 12000)
    show_employee("Jessa")