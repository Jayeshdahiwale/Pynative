'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Print first 10 natural number using while loop
'''

def print_first_ten_num():
    """
    info : It prints the first ten natural number
    param: It doesn't take ny param
    :return: Function doesn't return anything
    """
    i = 1
    while True :
        print(i)
        i += 1
        if i == 11:
            break

if __name__ == "__main__":
    print_first_ten_num()
