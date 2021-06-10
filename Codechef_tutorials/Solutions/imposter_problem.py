n=input()
n=int(n)

locations = []

for i in range(0,n):
    l=input()
    l=l.split(' ')

    for j in range(10):
        if l[j]=='I':
            locations.append(j)
for i in locations:
    print(i)