'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: Check the given inputs whether
they are equal to their reversed order or not.
'''

def equal_reverse(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(equal_reverse("madam"))
print(equal_reverse("tacocat"))
print(equal_reverse("utrecht"))
print(equal_reverse("marlboro"))