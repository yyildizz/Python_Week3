
"""This program receives strings and return whether this strings are equal to their reversed order"""
def ters(str_in):
    str_in=list(str_in)
    str1=[]
    lenght=len(str_in)
    i=0
    while i <lenght :
        str1.append(str_in[(lenght-i)-1])
        i+=1
    if str1==str_in:
        return True
    else:
        return False

def sent_to_exec(*args):
    result = []
    for i in args:
        result.append(ters(i))
    print("Words    :",*args)
    print ("reverse  :",*result)

sent_to_exec("merhaba","madam","tacocat","saat","seyyah")






