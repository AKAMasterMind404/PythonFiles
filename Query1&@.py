main1=[]
query=[]
print('Press enter to exit')
while True:
    ip=input('Enter main strings here:')
    if ip!='':
        main1.append(ip)
    else:
        break
print('#########')
while True:
    ip=input('Enter query strings here:')
    if ip!='':
        query.append(ip)
    else:
        break
tot=[]
for i in query:
    x=0
    for j in main1:
        if j==i:
            x+=1
    tot.append(x)
print(tot)