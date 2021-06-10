from itertools import combinations as c
import math

nums=int(input())
alpha=input().split()
indices=[]
alphaLength=len(alpha)
for i in range(alphaLength):
    if alpha[i]=='a':
        indices.append(i+1)

# print(indices)
numtuple=int(input())
l=c(range(1,nums+1),numtuple)
p,s=0,0
for i in l:
    # print(i)
    for j in indices:
        if j in i:
            p+=1
            break
    s+=1
print('%.3f'%(p/s))