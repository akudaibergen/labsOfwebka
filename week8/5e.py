ok=False
a=[]
n=(input("Number of array: "))
for i in range(int(n)):
    a.append(int(input()))
for i in range(int(n)):
    if i>0:
        if a[i] > 0 and a[i - 1] > 0:
            ok = True
            break
        elif a[i] < 0 and a[i - 1] < 0:
            ok = True
            break
if ok==True:
    print("YES")
else:
    print("NO")
