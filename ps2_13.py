n=int(input())
s=0
t=n
while t>0:
	a=t%10
	t=t//10
	s=s+(a**2)
print(s)
