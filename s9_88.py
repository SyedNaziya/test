def LCM(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while (True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater=greater+1
    return lcm
n1=int(input())
n2=int(input())
print(LCM(n1,n2))
