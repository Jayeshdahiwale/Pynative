'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Display elements of the list at odd index
'''

def odd_index(sequence):
    """
    info : It prints the elements at odd index
    param: It takes the list as a parameter
    :return: It does't return anything
    """
    for i in range(1,len(sequence),2):
        print(sequence[i])
if __name__ == "__main__":
    odd_index([10,20,30,40,50])
