def number():
    x = []
    y = input("please enter number : ")
    for i in range (len(y)):
        x.append(int(y[i]))
    count = 0
    for i in range (len(y)):
        if x[i] == 0:
            continue
        else:
            if int(y) % x[i] == 0:
                count += 1
    return print(count)
number()