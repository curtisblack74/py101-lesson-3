'''
For this practice problem, write a program that outputs The Flintstones Rock!
10 times, with each line prefixed by one more hyphen than the line above it.
The output should start out like this:

-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
'''

string_value = "The Flintstones Rock!"
counter = 0 

while counter <=10:
    string_value = "-" + string_value
    counter += 1
    print(string_value)


