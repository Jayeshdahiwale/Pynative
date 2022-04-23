'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Disply the numbers from a list
'''

def display_numbers(sequence):
    """
    info : This function displays the number from the list [The number must be divisible by 5,if number >50 skip it,
    if number greater than 500 stp the loop]
    param: It takes the list,tuple,set as a param
    :return: It doesn't return anything
    """
    for number in sequence:
        if number > 150:
            continue
        elif number >500:
            break
        else:
            print(number)
if __name__ == "__main__":
    display_numbers([1,23,4,5])