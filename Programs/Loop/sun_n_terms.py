'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Funtion calculates the sum of series upto n terms
'''

def sum_numbers(n):
    """
    info : It sum up the series till nth term
    param: It takes the num as a parameter
    :return: It does't return anything
    """
    two = "2"
    sum = 0
    for i in range(1,n+1):
        sum = sum +  int(two*i)
    return sum
if __name__ == "__main__":
    print(sum_numbers(5))

