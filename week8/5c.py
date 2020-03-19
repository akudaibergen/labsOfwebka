a=[]
c=0
n=(input("Number of array: "))
for i in range(int(n)):
    a.append(int(input()))
    if a[i]>0:
        c+=1;
print(c)