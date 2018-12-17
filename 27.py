num2=int(raw_input())
sum = 0
temp = num2
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num2 == sum:
   print("yes")
else:
   print("no")
