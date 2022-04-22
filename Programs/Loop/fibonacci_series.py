'''
@Author: Jayesh
@Date: 2021-02-11 18:00:30
@Last Modified by: Jayesh
@Last Modified time: 2021-02-11 18:00:30
@Title : Display fibonacci series upto 10
'''

a = 1
b = 1
for i in range(10):
    if i == 0:
        print(a,end =" ")
    elif i ==1:
        print(b,end=" ")
    else:
        temp = b
        b = a+b
        a = temp
        print(b,end=" ")


