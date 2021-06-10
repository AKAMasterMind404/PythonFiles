import operator

listOfEndPoints = []
listOfRequests = []
e1 = {}
with open('kittens.in.txt', 'r') as inputFile:
    V, E, R, C, X = map(int, inputFile.readline().strip().split())
    videoSizes = list(map(int, inputFile.readline().strip().split()))
    for eID in range(E):
        datacenterLatency, caches = map(int, inputFile.readline().strip().split())
        for cL in range(caches):
            cacheServerNumber, cacheLatency = map(int, inputFile.readline().strip().split())
            e1[eID, cL] = [datacenterLatency, cacheServerNumber, cacheLatency, X]
        if caches != 0:
            listOfEndPoints.append(e1)
    for request in range(R):
        vid, eid, numr = map(int, inputFile.readline().strip().split())
        listOfRequests.append([eid, vid, numr])
# print(sorted(listOfEndPoints[0].values(),key=operator.itemgetter(2)))
a = []
b = []
for i in sorted(listOfRequests, key=operator.itemgetter(2), reverse=True):
    c = 0
    if (videoSizes[i[1]] < X):
        try:
            while (videoSizes[i[1]] > sorted(listOfEndPoints[i[0]].values(), key=operator.itemgetter(2))[c][3]):
                c = c + 1
            if (sorted(listOfEndPoints[i[0]].values(), key=operator.itemgetter(2))[c][3] - videoSizes[i[1]] >= 0):
                sorted(listOfEndPoints[i[0]].values(), key=operator.itemgetter(2))[c][3] = \
                sorted(listOfEndPoints[i[0]].values(), key=operator.itemgetter(2))[c][3] - videoSizes[i[1]]
                a.append(sorted(listOfEndPoints[i[0]].values(), key=operator.itemgetter(2))[c][1])
                b.append(i[1])
        except:
            pass
# print(a)
# print(b)

with open('output.txt', 'w') as op:
    c = {}
    # print(len(set(a)))
    op.write(str(len(set(a))))
    op.write('\n')
    appeared = []
    for i in a:
        if i not in appeared:

            op.write(f'{i} ')
            for j in b:
                op.write(f'{j} ')
            op.write('\n')
            appeared.append(i)
