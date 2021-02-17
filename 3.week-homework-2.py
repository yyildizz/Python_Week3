"""
reading_number
"""
def reading_number():
    while True:
        x = input("please enter two digit number : ")
        y = int(x)
        number_0_10= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        number_10_20= ["ten", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        number_20_90= ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
        if 9<y<20 :
            return print(x, "------>", number_10_20[int(x[1])])
        elif 19<y<100 :
            return print(x, "------>", number_20_90[int(x[0])-2], number_0_10[int(x[1])])
        else:
            continue
reading_number()