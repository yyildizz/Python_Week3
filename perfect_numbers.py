'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: Finding perfect numbers between 1 and 1000.
Check perfect numbers between 1 and 1000 and
find the sum of the perfect numbers using reduce and filter functions.
'''

from functools import reduce
def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n
n = 2
numbers=[]
for n in range(1000):
    if perfect_number(n):
        numbers.append(n)
print("The perfect numbers between 1 an 1000 are",numbers)
result = (reduce(lambda x,y: x + y,numbers))
print(f"Sum of the perfect numbers between 1 an 1000 is: {result}")