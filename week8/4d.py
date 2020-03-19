a = int(input("Number is "))
i = 1
ok=False
while i<=a:
    if a==i:
        ok=True
    i*=2
if ok==False:
    print("NO")
else:
    print("YES")