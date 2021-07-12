n1, n2, n3 = map(int, input().split())

l = len({n1, n2, n3})

if l == 1:
    print("Equilateral")
elif l == 2:
    print("Isoceles")
elif l == 3:
    print("Scalene")
