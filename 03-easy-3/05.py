'''
The following function unnecessarily uses two return statements to return boolean values. 
Can you rewrite this function so it only has one return statement
and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
'''

#Option 1
def is_color_valid(color):
    return color == "blue" or color == "green"

#Option 2
def is_color_valid(color):
    return color in ["blue", "green"]