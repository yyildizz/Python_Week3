'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: Taking different words with hypen(-) in between them
and sorts the words in alphabetical order, adds hyphen icon (-) between them,
gives the output of the sorted words.
'''


def alphabetical_order():
    words = input("Enter different words with hypen (-) in between them:\n").split("-")
    sorted_words = sorted(words)

    for i in sorted_words:
        if i != sorted_words[-1]:
            print(i, end='-')
        else:
            print(i)


alphabetical_order()