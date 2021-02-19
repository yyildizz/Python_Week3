"""
Write a function that outputs the transcription of an input number with two digits.
Example:
28---------------->Twenty Eight
"""

def read_number():
    while True:
        x = int(input("Enter two digit number : "))

        nums_1to9 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        nums_teen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        nums_10s = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if 10 <= x < 20:
            print(x, "------>", nums_teen[x % 10])
            break
        elif 20 <= x < 100:
            print(x, "------>", nums_10s[x // 10], nums_1to9[x % 10])
            break
        else:
            print("Invalid data, please try again\n")

read_number()