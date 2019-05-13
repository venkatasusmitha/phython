def odddig():
	n=int(input())
	p1=[]
	while(n!=0):
		p1.append(n%10)
		n//=10
	for i in range(len(p1)-1,-1,-1):
		if p[i]%2!=0:
			print(p1[i]),
try:
	odddig()
except:
	print('invalid')
