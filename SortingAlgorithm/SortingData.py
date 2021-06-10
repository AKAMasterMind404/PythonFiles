def sort(list1):
    def splitIt(ip):
        l = []
        z = 0
        while z < len(ip):
            if ip[z] != ' ':
                c = ''
                try:
                    while ip[z] != ' ':
                        c += ip[z]
                        z += 1
                    l.append(int(c))
                except IndexError:
                    l.append(int(c))
            else:
                z += 1
        return l
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

    def smallestFinder(list1):
        smallest = list1[0]
        for i in list1:
            if i <= smallest:
                smallest = i
        return smallest

    def elementRemover(list, element):
        l = []
        removed = False
        z=0
        # while z<len(list):
        #     if list[z]==element:
        #         break
        #     else:
        #         l.append(list[z])
        # l.extend(list[z+1::])
        for i in list:
            if i == element and removed == False:
                removed = True
            elif i != element:
                l.append(i)
            elif i == element and removed == True:
                l.append(i)
        return l

    if type(list1)==str:
        list1 = splitIt(list1)
    newlist = []
    l = len(list1)
    while l>0:
        s=smallestFinder(list1)
        newlist.append(s)
        list1=elementRemover(list1,s)
        l-=1
    return newlist