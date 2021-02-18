'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
'''
Write a function that filters all the unique(unrepeated) elements of a given list.

Example:

Function call: unique_list([1,2,3,3,3,3,4,5,5])

Output : [1, 2, 3, 4, 5]
'''
def unique_list(liste):
    list1 = set(liste)
    return print(list(list1))

unique_list([1,2,3,55,3,3,25,45,3,4,5,5])