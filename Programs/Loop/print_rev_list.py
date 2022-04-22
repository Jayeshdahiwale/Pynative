'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Prints the reverse list
'''

def reversed_list(sequence):
    """
    info : It prints the reverse list
    param: It takes the list as a parameter
    :return: It does't return anything
    """
    for i in reversed(sequence):
        print(i)
if __name__ == "__main__":
    reversed_list([10,20,30,40,50])
