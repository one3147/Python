import math
a = int(input())
b = int(input())
min = 10001
sum = 0
for x in range(a,b + 1):
    if(math.sqrt(x) == int(math.sqrt(x))):
        sum += x
        if(x < min):
            min = x

if(min == -1 and sum == 0):
    print("-1")
else:
    print(sum,min)
    
