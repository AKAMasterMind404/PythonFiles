i=int(input('Enter decimal number:'))
a=[]
while int(i)>=0:
    if i==1:
        a.append(1)
        break
    else:
        a.append(i%2)
        i=int(i/2)
x=len(a)-1
ans=''
while x>=0:
    ans+=str(a[x])
    x-=1
print(ans)