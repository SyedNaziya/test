array = list()
num = input()
for i in range(int(num)):
    n = input()
    array.append(int(n))
print (array)
k=int(input())
if k in array:
	print("Yes")
else:
	print("No")
