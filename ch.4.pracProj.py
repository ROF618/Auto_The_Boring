"""

Practice Projects
For practice, write programs to do the following tasks.

Comma Code
Say you have a list value like this:


spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

"""


spam = ['apples', 'bananas', 'tofu', 'cats']

def Comma_Sep(l):
    Sep_List = ""
    for char in range(len(l)):
        if char == len(l) - 1:
            Sep_List = Sep_List + " and " + l[char]
        elif char == 0:
            Sep_List = Sep_List + l[char]
        else:
            Sep_List = Sep_List + ", " + l[char]
    return Sep_List
print(Comma_Sep(spam))
