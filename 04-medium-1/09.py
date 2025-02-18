'''
Consider these two simple functions:

What will the following function invocation return?
bar(foo())
'''

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

print(bar(foo()))

'''
The function will return 'False'. foo() returns 'yes' which is then the input
for the bar() function. By doing so, this changes the parameter param to be 
'yes'. The expression (param == "no") returns False. Due to the 'and' operator, 
(foo() or "no") is not evaluated as the first part already returns False
'''