s=raw_input()
b=len(s)
c=list(s)
if c%2==0:
    x=c/2 - 1
    a[x]='*'
    a[x+1]='*'
else:
    x=c/2 - 1
    a[x+1]='*'
print "".join(a)
