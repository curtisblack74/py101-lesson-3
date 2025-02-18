'''
What will the following two lines of code output?
'''
print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)

'''
The first line prints 0.89999999
The second line prints False
The reason for this is that the program uses floats which has floating point
precision errors. This means that some decimal numbers cannot be precisely
represented in binary, leading to small precision errors
'''