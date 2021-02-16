'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?: The transcription of an input number with two digits.
'''
num1_to_9 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
num10_to_19 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num20_to_90 = ['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']

def reading_number(num):

    if num == 0:
        return "zero"
    elif 1 <= num <= 9:
        return num1_to_9[num]
    elif 10 <= num <= 19:
        return num10_to_19[num]
    elif 20 <= num <= 99:
        if num % 10 == 0:
            return num20_to_90[(num//10)-2]
        else:
            x = num20_to_90[(num//10)-2] +" "+ num1_to_9[num%10]
            return x
    else:
       return "Out of range"
sayi = int(input("Enter a number:\n"))
print(sayi,"------->",reading_number(sayi))