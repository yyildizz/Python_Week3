'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''

def capitalize():
    low_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_letter= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    name = input("What is your name? ").split(" ")
   
    for i in range(len(name)):
        print(f"{upper_letter[low_letter.index(name[i][0])]}{name[i][1:]}",end=" ")

        #print(f"{name[i][0].upper()}{name[i][1:]}",end=" ")
  
capitalize()

'''
# Alternatif çözüm


def capitalize():
    name = input("What is your name? ").split(" ")
    #new_name = name.split(" ")
    for i in range(len(name)):

        print(f"{name[i][0].upper()}{name[i][1:]}",end=" ")
  
#uppered_pets = list(map(str.upper, name))
capitalize()
'''
