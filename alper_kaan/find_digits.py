'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''

def find_digits():
    n = input("incelemek istediğiniz sayıyı girin: ")
    num= []
    for i in n:
        if i != "0":
            if int(n) % int(i) == 0:
                num.append(i)
    
    print(len(num))


find_digits()


    