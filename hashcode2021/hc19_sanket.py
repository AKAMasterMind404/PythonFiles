import operator
from itertools import combinations as c

with open('19ip.txt', 'r') as ip:
    photos = int(ip.readline().strip())
    photoData = []
    for pic in range(photos):
        data = ip.readline().strip().split()
        orientation = data[0]
        numTags = int(data[1])
        tags = data[2::]
        numTags = int(numTags)
        photoData.append([
            pic,  # 0 id of the picture
            orientation,  # 1 the orientation of the picture
            numTags,  # 2 number of tags in this picture
            tags  # 3 list containing the tags of a picture
        ])
iv = []


def combineiv(photo1, photo2):
    tags1 = photo1[3]
    tags2 = photo2[3]
    tg = len(photo1)
    for tag in tags2:
        if tag not in tags1:
            tags1.append(tag)
            tg += 1
    return [(photo1[0], photo2[0]), 'V', tg, tags1]


def interest(a, b):
    '''c1,c2,c3=0,0,0
    for i in a[3]:
        for j in b[3]:
            if(i in a[3] and i not in b[3]):
                c2+=1
            elif(i==j):
                c1+=1
            else:
                c3+=1'''
    s1 = set(a[3])
    s2 = set(b[3])
    return min(len(s1.intersection(s2)), len(s1 - s2), len(s2 - s1))


def commonRatio(photo1, photo2):
    tags1 = photo1[3]
    tags2 = photo2[3]
    common = [value for value in tags1 if value in tags2]
    uncommon = [value for value in tags1 if value not in tags2]
    return [[photo1[0], photo2[0]], len(common), len(uncommon)]


sl = []
for i in photoData:
    if i[1] == 'H':
        sl.append(i)
    else:
        iv.append(i)
while len(iv) > 0:
    if len(iv) == 1:
        iv.pop(0)
    else:
        comboiv = list(c(iv, 2))
        vertCombList = []
        for i in comboiv:
            vertCombList.append(commonRatio(i[0], i[1]))
        vertCombList.sort(key=operator.itemgetter(2), reverse=True)
        x = vertCombList[0][0]
        for i in iv:
            if i[0] == x[0]:
                tempImg1 = i
            if i[0] == x[1]:
                tempImg2 = i
        temp = combineiv(tempImg1, tempImg2)
        sl.append(temp)
        for i in iv:
            if i[0] in temp[0]:
                ind = iv.index(i)
                iv.pop(ind)
print(sl)
score = 0
for i in range(len(sl) - 1):
    score += interest(sl[i], sl[i + 1])
print(score)
