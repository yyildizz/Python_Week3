"""
Write a function that controls the given inputs whether they are equal to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
"""

def reversed(str):

    print (str == str[::-1])

reversed(input("Input the word\n"))
