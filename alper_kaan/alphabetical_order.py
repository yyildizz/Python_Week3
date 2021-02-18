'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
'''
Write a function that takes an input of different words with hyphen (-) in between them and then:

sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. Example:

Input >>> green-red-yellow-black-white

Output >>> black-green-red-white-yellow
'''
def make_list():
    newlist =input("çizgi koyarak eleman oluştur\n").split("-")
    newlist.sort()
    return print(*newlist,sep="-")


make_list()


