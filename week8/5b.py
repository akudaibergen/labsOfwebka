a=[]
n=(input("Number of array: "))
for i in range(int(n)):
    a.append(int(input()))
for i in range(int(n)):
    if a[i]%2==0:
        print(a[i])