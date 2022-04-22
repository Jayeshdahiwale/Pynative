'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Find multiplication table
'''

def multiplication_table(num):
    """
    info : It calcultes the multiplication table
    param: It takes the number of whose we will be calculating the table
    :return: It doesn't return anything
    """
    for i in range(1,11):
        print(num*i)
if __name__ == "__main__":
    multiplication_table(5)
