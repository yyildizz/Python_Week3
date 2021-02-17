"""alphabetical_order"""
def alphabetical_order(x):
    x1=x.split("-")
    x1.sort()
    x2="-".join(x1)
    print(x2)
x="green-red-yellow-black-white"
alphabetical_order(x)