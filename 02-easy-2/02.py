'''
Given a number and a list, determine whether the number is included in the list.
'''

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

def find_number(number):
    if number in numbers:
        print(True)
    else:
        print(False)

find_number(number1)
find_number(number2)