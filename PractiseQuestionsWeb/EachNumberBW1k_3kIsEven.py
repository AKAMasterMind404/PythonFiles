fin=[]
for i in range(1000,3001):
    num=str(i)
    x=0
    for j in num:
        if int(j)%2==0:
            x+=1
    if x==len(num):
        fin.append(num)
print(fin,len(fin))