"""perfect_number"""
a, d = 0, []
for i in range (1,1001):
    c = []
    for a in range(1,i):
        if i%a == 0:
            c.append(a)
        else:
            continue
    if sum(c)==i:
        d.append(i)
print("1-1000 between perfect number : ",d)