def xorIS(a,b):
    if a==1 and b==1:
        return 0
    elif a==0 and b==1:
        return 1
    elif a==1 and b==0:
        return 1
    else:
        return 0
a=int(input("Number a is "))
b=int(input("Number b is "))
print(xorIS(a,b))