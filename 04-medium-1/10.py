'''
In Python, every object has a unique identifier that can be accessed using the id() function.
This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime.
For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value.
This is known as "interning".

Given the following code, predict the output:
'''

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

'''
This will print True. 'a' and 'c' will have the same object in memory, which results in their ids being the same
Due to the concept of interning, 'b' has the same id as 'c' and 'a'.
Since all the ids for the variables are the same, the program outputs True
'''