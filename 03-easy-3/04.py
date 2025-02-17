'''
What will the following code output?
'''
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

'''
This will output [{"first": 42"}, {"second": "value2"}, 3, 4, 5]
because .copy() creates a shallow copy of my_list1. Although this creates a new list
the dictionary objects are the same across the two lists
'''
