from itertools import combinations as c
from itertools import permutations as p

a=[1,2,3]

b1=p(a,3)
b2=c(a,3)
l=[]
for i in b2:
    if i not in l:
        l.append(i)
        print(i)
    if i[::-1] not in l:
        l.append(i[::-1])
        print(i[::-1])