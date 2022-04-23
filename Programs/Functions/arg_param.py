"""

@Author: Jayesh Dahiwale
@Date: 2022-04-13 07:38:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-12 19:00:00
@Title : Calling a function with args

"""
def func1(*args):
    for i in args:
        print(i)

if __name__ == "__main__":
    func1(20, 40, 60)
