def _sum(array,n1):
    return(sum(array))
array = list()
num = input()
for i in range(int(num)):
    n = input()
    array.append(int(n))
n1=len(array)
ans=_sum(array,n1)
print(array)
print(ans)
