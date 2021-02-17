"""unique_list"""
def unique_list(x):
    y= set(x)
    z=list(y)
    z.sort()
    return print(z)
x=[1,10,100,1000,523,623,6,7,8,9,6,9,9,100]
unique_list(x)