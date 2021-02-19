"""
Write a function that filters all the unique(unrepeated) elements of a given list.
Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output : [1, 2, 3, 4, 5]
"""

def unique_list(x):
    y = set(x)
    print(list(y))

unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5])
