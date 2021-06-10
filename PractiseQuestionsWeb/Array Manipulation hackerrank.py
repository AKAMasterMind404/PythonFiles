def arrayManipulation(n, queries):
    def inputToList(i):
        list1 = []
        z = 0
        while z < len(i):
            numatindex = str(i[z])
            if numatindex != ' ':
                try:
                    while i[z + 1] != ' ' and z < len(i) - 1:  # 15
                        numatindex += i[z + 1]
                        z += 1
                except IndexError:
                    if i[z] == ' ':
                        break
                list1.append(int(numatindex))
                z += 1
            else:
                z += 1
        return list1
    array = []
    for i in range(0, n):
        array.append(0)
    for i in queries:
        i=inputToList(i)
        a=int(i[0])
        b=int(i[1])
        r=int(i[2])
        for j in range(a-1,b):
            array[j]+=r
    return max(array)
print(arrayManipulation(5,['1 2 100','2 5 100','3 4 100']))
