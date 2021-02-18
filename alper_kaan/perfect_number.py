'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
'''
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000.

Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
'''


from functools import reduce

def custom_sum(first, second): #reduce için sayı toplamı
    return first + second


def check_perfect_number(liste):
    for j in liste: 
        newlist = [i for i in range(1,j+1)] 
        '''
        [1]
        [1, 2]
        [1, 2, 3]
        [1, 2, 3, 4]
        ...
        ...
        ...
        [1, 2, 3, 4,...,1000]
        ''' 
        
        divisors = [] #tam bölenler listesi
        
        for a in newlist:
            if  j % a == 0 and j !=a : # j : newlist 'in son elemanı
                divisors.append(a)
    
        if reduce(custom_sum,divisors,0) == j: # tam bölenleri toplamı newlist[-1] e eşit mi
            print(j," perfect number")
        

liste1000 = [i for i in range(1,1001)] # liste1000 = [1,2,3,4,...,1000]

check_perfect_number(liste1000)
