'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Prints prime number in a range
'''

def prime_numbers(start,end):
    """
    info : It prints the prime number between start and end
    param: It take start number and end number as parameter
    :return: It does'treturn nything
    """
    for i in range(start+1,end):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)
if __name__ == "__main__":
    prime_numbers(1,20)
