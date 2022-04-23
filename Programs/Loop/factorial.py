'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Factorial of a given number
'''

def factorial(num):
    """
    info : It calculates the factorial of a given number
    param: It takes the number s a param
    :return: It returns an integer tht is factorial
    """
    factorial =1
    for i in reversed(range(1,num+1)):
        factorial *= i
    return factorial
if __name__ == "__main__":
    print(factorial(5))
