if __name__ == '__main__':
    b = ''
    a = int(input())
    for _ in range(a + a - 1):
        b += input()
    b = b.replace('/', '//')
    print(eval(b))
