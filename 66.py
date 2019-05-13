num3= int(raw_input())
for i in range(2, int(num3/2)):
    if num3 % i  == 0:
        print("no")
        break
else:
    print("yes")
