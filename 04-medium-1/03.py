'''
Alyssa was asked to write an implementation of a rolling buffer.
You can add and remove elements from a rolling buffer.
However, once the buffer becomes full,
any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:

What is the key difference between these implementations?
'''

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

'''
In the first option, the program uses .append() to add on the new_element to
the buffer variable which mutates the original list
In the second option, the program concatenates buffer with the new_element and
does not mutate the original list but instead creates a new list and assigns
it to buffer
'''