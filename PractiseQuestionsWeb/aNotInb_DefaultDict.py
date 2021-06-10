ip=input().split()

n=int(ip[0])
m=int(ip[1])

a=[]
b=[]

for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

for _ in b:
    if _ not in a:
        print(-1)
    else:
        for i in range(len(a)):
            if a[i]==_:
                print(i+1,end=' ')
        print()