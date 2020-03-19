ok=False
a=[]
n=int(input("Number of array: "))

for i in range(int(n)):
    a.append(int(input()))
for i in range(n-1, -1, -1):
    print(a[i])

