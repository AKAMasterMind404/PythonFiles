def mergeSortIterative(l1):
    def merge(l1, l2):
        p1 = 0
        p2 = 0
        srtd = []
        while len(srtd) != len(l1) + len(l2):
            if p1 == len(l1):
                srtd.append(l2[p2])
                p2 += 1
            elif p2 == len(l2):
                srtd.append(l1[p1])
                p1 += 1
            else:
                if l1[p1] > l2[p2]:
                    srtd.append(l2[p2])
                    p2 += 1
                else:
                    srtd.append(l1[p1])
                    p1 += 1
        return srtd

    for i in range(0,len(l1)-1):
        if type(l1[i])==int:l1[i] = [l1[i]]
        if type(l1[i+1]) == int:l1[i+1] = [l1[i+1]]

        l1[i+1]=merge(l1[i],l1[i+1])

    return (l1[len(l1)-1])