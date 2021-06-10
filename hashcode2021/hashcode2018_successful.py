import operator
import math

with open('e_high_bonus.in', 'r') as ip:
    r, c, numVehicles, numRides, bonus, t = map(int, ip.readline().strip().split())
    #    print(r,c,numVehicles,numRides,bonus,t)
    rideInfo = []
    for ride in range(numRides):
        a, b, x, y, start, end = map(int, ip.readline().strip().split())
        rideInfo.append(
            [
                ride,  # 0 ride number
                [a, b],  # 1 start coordinates
                [x, y],  # 2 end coordinates
                start,  # 3 start ride by
                end,  # 4 end ride by
            ]
        )
# for i in rideInfo:
#    print(i)
cs = []
'''for i in range(numVehicles):
    x=[]
    for j in range(r):
        y=[]
        for k in range(c):
            y.append(0)
        x.append(y)
    cs.append(x)'''
mo = []
for i in range(numVehicles):
    cs.append([i, [0, 0], 0])
    mo.append([])
count = 0
score = 0
for i in sorted(rideInfo, key=operator.itemgetter(3)):
    temp = [math.inf, [math.inf, math.inf], i[4]]
    for j in range(numVehicles):
        if (abs(cs[j][1][0] - i[1][0]) < temp[1][0] and abs(cs[j][1][1] - i[1][1]) < temp[1][1] and abs(
                cs[j][1][0] - i[1][0]) + abs(cs[j][1][1] - i[1][1]) + abs(i[1][0] - i[2][0]) + abs(i[1][1] - i[2][1]) +
                cs[j][2] < temp[2] and abs(cs[j][1][0] - i[1][0]) + abs(cs[j][1][1] - i[1][1]) + abs(
                        i[1][0] - i[2][0]) + abs(i[1][1] - i[2][1]) + cs[j][2] < t):
            temp = cs[j]
    if (temp[0] != math.inf):
        print("ride ", i[0], " was done by vehicle ", temp[0])
        cs[temp[0]][2] += abs(cs[j][1][0] - i[1][0]) + abs(cs[j][1][1] - i[1][1])
        print("Vehicle reaches start at ", cs[temp[0]][2])
        if (cs[temp[0]][2] <= i[3]):
            cs[temp[0]][2] = i[3]
            count = count + 1
            score = score + bonus
            print("Bonus received")
        cs[temp[0]][2] += abs(i[1][0] - i[2][0]) + abs(i[1][1] - i[2][1])
        score = score + abs(i[1][0] - i[2][0]) + abs(i[1][1] - i[2][1])
        cs[temp[0]][1] = i[2]
        mo[temp[0]].append(i[0])
print("score:", score)
file = open('out.txt', 'w+')
c = 0
for i in mo:
    print()
    file.write(f"{str(c) + ' ' + ' '.join(list(map(str, i)))}\n")
    c += 1
    # c=c+1
file.close()
