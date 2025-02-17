'''
Write two different ways to remove all of the elements from the following list:
'''
numbers = [1, 2, 3, 4]

#Option 1
numbers[:] = []
print(numbers)

#Option 2
numbers.clear()
print(numbers)