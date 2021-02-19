"""
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
"""

def orderWords(words):
    wordList = words.split("-")
    wordList.sort()
    print("Output is:\n", ("-".join(wordList)))

orderWords(input("Input the words:\n"))