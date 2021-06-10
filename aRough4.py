input()
arr = list(map(int, input().split()))
d = {}
for i in range(len(arr)):
    if d.get(arr[i]):
        d[arr[i]].append(i+1)
    else:
        d[arr[i]]=[i+1]

q = int(input())
for i in range(q):
    num = int(input())

print(d)