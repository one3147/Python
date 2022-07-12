a = int(input())
b = int(input())
num = []
i = 1
while i ** 2 <= b:
    if a <= i ** 2 <= b:
        num.append(i ** 2)
    i += 1
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])
