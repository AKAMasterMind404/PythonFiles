x=['Abc','def','GHI','HGFJHF','GSGF','WEEF','GDFGDF','QEQOJX','SHONVV','WCCEC','IHNC']
n=len(x)
sumofascii=[]
for i in x:
    s=0
    for j in i:
       s+=ord(j)
    sumofascii.append(s)

orderedarray=[]
for i in x:
    orderedarray.append(None)

dic={}
z=0
for i in x:
    dic[i]=sumofascii[z]
    z+=1
def addresschecker(n,array1):
    if array1[n]==None:
        return 1
    else:
        return 0
for i in dic:
    asc=dic.get(i)
    tempad=asc%11
    print(i,tempad,'before')
    while True:
        see=addresschecker(tempad,orderedarray)
        if see==1:
            print(i,tempad,'after')
            print()
            break
        else:
            if tempad<10:
                tempad+=1
            elif tempad==10:
                tempad=0
    orderedarray[tempad]=i
print(dic)
print(orderedarray)