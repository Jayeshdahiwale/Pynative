'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Sum from 1 to given numbers
'''

def sum_natural_num(num):
    """
    info : It calcultes the sum from 1 to given number
    param: It takes the number upto which we want to calculate sum
    :return: It returns the sum
    """
    sum = 0
    for i in range(1,num+1):
        sum+=i
    return sum
if __name__ == "__main__":
    print(sum_natural_num(5))
