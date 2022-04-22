'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Reverse an integer number
'''

def reversed_number(number):
    """
    info : It prints the reverse list
    param: It takes the list as a parameter
    :return: It does't return anything
    """
    new_num = 0
    while(number != 0):
        rem = number % 10
        new_num = new_num * 10 + rem
        number = number//10
    return new_num

if __name__ == "__main__":
    print(reversed_number(1234))
