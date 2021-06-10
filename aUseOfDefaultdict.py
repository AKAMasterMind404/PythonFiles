from collections import defaultdict

l = defaultdict(lambda: 1)

l[1] = 1
l[2] = 2
l[3] = 3
l[4] = 4

print(l[5])
