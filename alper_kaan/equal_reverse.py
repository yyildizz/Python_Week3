'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
'''
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:

Input >>> madam, tacocat, utrecht

Output >>> True, True, False
'''
def equal_reverse():
    liste = input("listeyi aralarına virgül koyarak yazın: \n").split(",")
    print(liste)
    
    for i in liste:
        word = i.strip()
        if i != liste[-1]:
            if word == word[::-1]:
                print(True,end=",")

            elif word != word[::-1]:
                print(False,end=",")
        else:
            if word == word[::-1]:
                print(True)

            elif word != word[::-1]:
                print(False)

equal_reverse()

