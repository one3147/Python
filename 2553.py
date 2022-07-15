n=int(input())

result=1
for i in range(2,n+1):
    result*=i

result=str(result)[::-1]
for i in result:
    if i!='0':
        print(i)
        break
