def minOfFourth( a, b,c, d):
    if a<b and a<c and a<d:
        return a
    elif b<a and b<c and b<d:
        return b
    elif c<a and c<b and c<d:
        return c
    else:
        return d
a=int(input("Number a is "))
b=int(input("Number b is "))
c=int(input("Number c is "))
d=int(input("Number d is "))
print(minOfFourth(a,b,c,d))