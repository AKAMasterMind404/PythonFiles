charachters=['$','#','@']
small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']
large=[]
for i in small:
    large.append(i.upper())
numbers=[1,2,3,4,5,6,7,8,9,0]

passwords=['ABd1234@1','a F1#,2w3E*','2We3345']
valid=[]
for i in passwords:
    if len(i) in [6,7,8,9,10,11,12]:
        cc=0
        sc=0
        lc=0
        nc=0
        for j in i:
            if j==' ':
                break
            elif j in charachters:
                cc+=1
            elif j in small:
                sc+=1
            elif j in large:
                lc+=1
            else:
                try:
                    k = int(j)
                    nc+=1
                except ValueError:
                    nc+=0
        check=[cc,sc,lc,nc]
        if 0 not in check:
            valid.append(i)
print(valid)