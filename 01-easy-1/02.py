'''
How can you determine whether a given string ends with an exclamation mark 
(!)? Write some code that prints True or False depending on whether the string 
ends with an exclamation mark
'''


str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False


def exclamation_finder(string_value):
    print(string_value.endswith('!'))

exclamation_finder(str1)
exclamation_finder(str2)
 

