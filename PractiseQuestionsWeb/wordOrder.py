num=int(input())

dic1={}

for i in range(num):
    theInput=input()
    if theInput in dic1:
        dic1[theInput]+=1
    else:
        dic1[theInput]=1

print(len(dic1))
for i in dic1:
    print(dic1[i],end=' ')