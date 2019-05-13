n1=int(raw_input())
factor=0
for i in range(1,n1):
  if n1%i==0:
    factor=i
if factor>1:
  print "yes"
elif n1==1:
  print "prime"
else:
  print "no"
