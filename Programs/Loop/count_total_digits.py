'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Count total digits in a number
'''

def total_digits(number):
    """
    info : This function calculates the total digits inn a number
    param: It takes a number as  parameter
    :return: It returns the total digits in a number
    """
    digits = 0
    while number != 0 :
        digits += 1
        number = number//10
    return digits
if __name__ == "__main__":
    print(total_digits(234))