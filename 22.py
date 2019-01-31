num2 = int(input())
 
temp = num2
rev = 0
 
while temp != 0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10
 
if num2 == rev:
    print("yes")
else:
    print("no")
