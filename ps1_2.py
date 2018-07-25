def fact(x1):
    if x1==1:
        return 1
    else:
        return (x1*fact(x-1))
n=int(input())
print(fact(n))
