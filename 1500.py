a,b, = input("").split()
a = int(a)
b = int(b)
c = a // b
d = a % b
n = 1
while b > 0:
    if d > 0:
        n *= c + 1
        d -= 1

    else:
        n *= c
    b -= 1

print(n)
