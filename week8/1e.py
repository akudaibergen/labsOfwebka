v=input("Velocity")
t=input("Time")
s=109-(int(v)*int(t))
if s>0:
    print(s)
else:
    s=-s
    print(s)