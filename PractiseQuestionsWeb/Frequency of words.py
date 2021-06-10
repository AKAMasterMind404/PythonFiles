i=input()
def listofwords(i):
    z = 0
    wordlist = []
    while z<len(i):
        w=''
        if i[z]==' ':
            z+=1
        else:
            if z!=len(i)-1:
                while i[z]!=' ' and z<len(i)-1:
                    w+=i[z]
                    z+=1
            if i[z]!=' ':
                w+=i[z]
                z+=1
        if w!='':
            wordlist.append(w)
    return wordlist

i=listofwords(i)

unique=[]
ans={}
for j in i:
    if j not in unique:
        ans[j]=1
        unique.append(j)
    else:
        ans[j]=int(ans.get(j)+1)
print(ans)