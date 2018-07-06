x=int(input())
c=0
t=x
while t>0:
    a=t%10
    t=t//10
    c=c+(a**3)
if x==c:
    print("Yes")
else:
    print("No")
