'''
Show two different ways to create a new string with "Four score and " 
prepended to the front of the string referenced by famous_words.
'''

famous_words = "seven years ago..."

#Option 1
new_string_1 = f'Four score and {famous_words}'
print(new_string_1)

#Option 2
other_string = 'Four score and '
new_string_2 = other_string + famous_words
print(new_string_2)

#Option 3
new_string_3 = "Four score and " + famous_words
print(new_string_3)