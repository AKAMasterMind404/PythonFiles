for _ in range(int(input())):
    input()
    l = list(map(int,input().strip().split()))
    if len(set(l)) == len(l):
        print("YES")
    else:
        print("NO")