a=[]
c=0
n=(input("Number of array: "))
for i in range(int(n)):
    a.append(int(input()))
for i in range(int(n)):
    if a[i-1]<a[i]:
        c+=1
print(c)