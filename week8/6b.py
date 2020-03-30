def setepen(a,b):
    for i in range(b-1):
        a*=a
    return a
a=int(input("Number a is "))
b=int(input("Number b is "))
print(setepen(a,b))
