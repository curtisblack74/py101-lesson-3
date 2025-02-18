'''
One day, Spot was playing with the Munster family's home computer,
and he wrote a small program to mess with their demographic data:

After writing this function, he typed the following code:
mess_with_demographics(munsters)

Before Grandpa could stop him, Spot hit the Enter key with his tail
Did the family's data get ransacked? Why or why not?
'''

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


'''
Yes it does impact the data because dictionaries are mutable in Python
When a dictionary is passed to the function, a reference to the dictionary is
passed instead of a copy. As such, each iteration directly impacts the age
and gender values
'''