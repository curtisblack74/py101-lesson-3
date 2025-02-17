'''
Write two distinct ways of reversing the list without mutating the original list.
'''

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

new_list_1 = numbers[::-1]
print(new_list_1)

new_list_2 = list((reversed(numbers)))
print(new_list_2)