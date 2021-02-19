"""
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000.
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
"""

def is_Perfect(num):
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i
    return total == num

perfects = []
for i in range(2,1000):
    if is_Perfect(i):
        perfects.append(i)

print("The perfect numbers between 1 and 1000 is:\n", perfects)