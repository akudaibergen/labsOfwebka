c=0
a=[]
n=(input("Number of array: "))
for i in range(int(n)):
    a.append(int(input()))
for i in range(int(n)):
    if i>0 and i<4:
        if a[i] > a[i-1] and a[i] > a[i+1]:
            c+=1
print(c)

