def occurance(a,b):
    occ=0
    z=0
    while z+len(a)<=len(b):
        sub=b[z:z+len(a)]
        z+=1
        if a==sub:
            occ+=1
    return occ

t = int(input())
for i in range(1, t+1):
    y = 0
    n, k = input().split()
    l1=list(input().split())
    l=[]
    for m in range(int(k),0,-1):
        l.append(str(m))
    y=occurance(l,l1)
    op = "Case #" + str(i) + ": " + str(y)
    print(op)