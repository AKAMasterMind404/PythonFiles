# CONTEST NAME: Educational Codeforces Round 137 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1743

for _ in range(int(input())):
    a,b,c = map(int,input().strip().split())
    if (sum([b,c]) == a) or (sum([b,a]) == c) or (sum([a,c]) == b):
        print("YES")
    else:
        print("NO")