'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Print the number pyramid pattern
'''

def print_number_pattern(num):
    """
    info : It prints the number pattern
    param: It takes the number upto which we want to print pattern
    :return: It does't return anything
    """
    for i in range(num):
        for j in range(i+1):
            print(j+1,end=" ")
        print()
if __name__ == "__main__":
    print_number_pattern(5)
