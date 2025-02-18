'''
What do you think the following code will output?
How can you reliably test if a value is nan?
'''

nan_value = float("nan")

print(nan_value == float("nan"))

'''
The print function will output False because NaN values do not equal each other
They represent undefined values and therefore Python ensures NaN != NaN

You can reliably test if a value is NaN using math.isnan()
'''