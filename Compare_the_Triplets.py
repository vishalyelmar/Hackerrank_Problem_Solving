def CompareTriplets(a,b):
    alice =0
    bob = 0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    return alice,bob
a=[]
for i in range(3):
    a.append(int(input()))
b=[]
for i in range(3):
    b.append(int(input()))
print(CompareTriplets(a,b))