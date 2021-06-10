from itertools import combinations as c
from itertools import permutations as p
import operator
from collections import namedtuple
import math
with open('2021submission/f.txt', 'r') as ip:
    duration, intersections, numStreets, numcars, bonus = map(int, ip.readline().strip().split())
    print(duration, intersections, numStreets, numcars, bonus)
    streetInfo = []

    for sID in range(numStreets):
        tIP = ip.readline().strip().split()
        # print(tIP)
        iStart, iEnd = int(tIP[0]), int(tIP[1])
        streetName = tIP[2]
        streetLength = int(tIP[3])

        streetInfo.append([
            sID,  # 0 street id
            [iStart,iEnd],  # 1 intersection at start and end
            streetName,  # 2 name of the street
            streetLength,  # 3 # Time taken for a car to cross the length of a street
        ])
    carInfo = []
    for car in range(numcars):
        tIP = ip.readline().strip().split()
        streetsToTravel = int(tIP[0])
        streets = tIP[1::]
        carInfo.append([
           car,  # 0 car number
           streetsToTravel,  # 1
           streets,  # 2
        ])
# for i in streetInfo:
#     print(i)
# for i in carInfo:
#     print(i)
count={}
for i in streetInfo:
    count.update({i[2]:(0,i[1][1])})
cc=count
for j in carInfo:
    path=[]
    for i in j[2]:
        for k in streetInfo:
            if(i==k[2]):
                path.append(k)
                count.update({i:(count[i][0]+1,count[i][1])})
    j.append(path)
print(count)
for i in carInfo:
    s=0
    for j in i[3]:
        s+=j[3]
    if(s>duration):
        carInfo.pop(carInfo.index(i))
    else:
        i.append(s)
inter=[]
interdt=[]
temp=[]
pp=False
for i in sorted(count,key=operator.itemgetter(0)):
    if(count[i][1] not in inter or pp==True and count[i][1]!=499):
        interdt.append(temp)
        temp=[]
        inter.append(count[i][1])
        temp.append((i,count[i][0]))
    else:
        if(count[i][0]!=0):
            temp.append((i,count[i][0]))
        else:
            pp=True
interdt.append(temp)
interdt.pop(0)
fg=open("output.txt","w+")
fg.write(str(len(inter))+"\n")
print(inter)
print(interdt)
for i in inter:
    fg.write(str(i)+"\n"+str(len(interdt[inter.index(i)]))+"\n")
    for j in interdt[inter.index(i)]:
        fg.write(' '.join([str(q) for q in j]) + "\n")