n1=raw_input().rstrip()
digits=[]
for c in n1:
    if c.isdigit():
        digits.append(c)
print ("".join(digits))
