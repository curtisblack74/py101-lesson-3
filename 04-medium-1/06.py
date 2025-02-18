'''
What is the output of the following code?
'''

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

'''
The code outputs 34 because mess_with_it() does not update the global name variable.
It instead creates a new variable, which is stored as new_answer, and returns 50
Therefore the answer variable remains unchanged
and the print function subtracts 8 from 42 to get 34
'''