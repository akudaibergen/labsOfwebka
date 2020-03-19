a=int(input("Number is "))
b=0
for i in range (1,a+1):
    if a%i==0:
        b=b+1
print(b)