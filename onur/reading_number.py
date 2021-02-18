""" This program takes a two digit number from user and prints the verbal expression
of the digits"""

#Function definitions
def convert_to_verbal(num_in):

    firt_digit_dict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
                         5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    Second_digit_dict = { 2: "Twenty", 3: "Thirty", 4: "Fourty",
                       5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

    up_to_19_dict = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                      15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

    str_out = ""

    if int(num_in) <10:
        number = list(num_in)
        j=int(number[1])
        str_out += firt_digit_dict.get(j)
        str_out+=" "
    elif int(num_in)<=19:
        j = int(num_in)
        str_out += up_to_19_dict.get(j)
        str_out += " "

    elif int(num_in)<=99 and int(num_in)%10!= 0:
        number = list(num_in)
        j = int(num_in[0])
        str_out += Second_digit_dict.get(j)
        str_out += " "
        j = int(num_in[1])
        str_out += firt_digit_dict.get(j)

    elif int(num_in)<=99 and int(num_in)%10== 0:
        number = list(num_in)
        j = int(num_in[0])
        str_out += Second_digit_dict.get(j)

    else:
        print("Out of range")
    print(str_out)


#variable definitions
number=""
check=True

#Program Starts Here
while check:
    number = (input("Please enter a two digit number :"))
    if len(number)!=2:
        print("What is your point!")
    else:
        check=False

convert_to_verbal(number)

