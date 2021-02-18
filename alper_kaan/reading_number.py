'''
Developer: Alper Kaan
Date: 14.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
'''
##################################################################################
'''
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
'''
def basamak ():
    single_digit = [" ","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
    less_20 = [" ","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    ten_digit = [" " ,"Twenty","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    
    number = int (input("yazdırmak istediğiniz sayıyı girin: "))

    onlar = number // 10 
    birler = number % 10

    if number < 11:
        print(f"{number} -------> {single_digit[number]}")
    elif 10 < number < 20:
        print(f"{number} -------> {less_20[number % 10]}")
    
    else:
        if birler != 0: 
            print(f"{number} -------> {ten_digit[onlar]} {single_digit[birler]}")
        else:
            print(f"{number} -------> {ten_digit[onlar]}")
while(True):   
    basamak()