import math
a=int(input("First number: "))
b=int(input("Second number: "))
for i in range(a,b):
    if math.sqrt(i)==round(math.sqrt(i)):
        print(i)