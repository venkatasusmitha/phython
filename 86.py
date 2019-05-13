s2=raw_input()
c=len(s2)
fct=0
for i in range(0,c):
    j=i+1
    while j<c:
        if ord(s2[i])==ord(s2[j]):
            fct=1
        j=j+1
if fct!=1:
    print "Yes"
else:
    print "No"
