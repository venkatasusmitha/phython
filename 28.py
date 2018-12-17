lower,upper=map(int,raw_input().split())
for num6 in range (lower,upper+1):
    order = len(str(num6))
    sum = 0
    temp=num6
    while temp>0:
        digit=temp%10
        sum +=digit**order
        temp//=10
        if num6==sum:
            print(num6),
