'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Prints the cube of all numbers
'''

def cube(sequence):
    """
    info : It prints the cube of every element in a list
    param: It takes the list as a parameter
    :return: It doesn't return anything
    """
    for i in sequence:
        print(i**3)
if __name__ == "__main__":
    cube([10,20,30,40,50])
