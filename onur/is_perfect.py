"""This program is written to check if a number is perfect which :
    positive integer that is equal to the sum of its proper divisors"""
from functools import reduce
#Function Definitions
#is_perfect() function returns a int if the argument number is a perfect number
#or a string that states out the argument is not a perfect number
def is_perfect(number):
    dividers = [1]
    total = 0
    if number < 0:
        print ("not perfect")
    else:
        for i in range(2,number):
            if number%i == 0:
                dividers.append(i)

        if number == sum(dividers):
            return (number)

        if len(dividers) == 1 or number != sum(dividers):
            return "number is not perfect"
#check() function is defined to be used as an argument function for filter()
def check(x):
    if type(x)==int:
        return x
#This part of code finds the sum of  perfect numbers in range(1000) with filter() + Reduce() functions
initial_list = []
for i in range(1000):
    initial_list.append(is_perfect(i))
sum=reduce((lambda x,y: x+y),list(filter(check, initial_list)))
print("Sum of perfect numbers up to 1000  :", sum)

