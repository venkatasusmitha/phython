n=int(raw_input())
factor=0
for i in range(1,n):
  if n%i==0:
    factor=i
if factor>1:
  print "yes"
elif n==1:
  print "prime"
else:
  print "no"
