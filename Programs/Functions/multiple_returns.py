"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Getting multiple returns from a function

"""
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
if __name__ == "__main__":
    res = calculation(40, 10)
    print(res)