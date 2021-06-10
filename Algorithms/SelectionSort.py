def selectionSort(array):
    l=len(array)
    for i in range(l):
        small=array[i]
        sindex=i
        for j in range(i,l):
            if array[j]<small:
                small=array[j]
                sindex=j
        array[i],array[sindex]=array[sindex],array[i]
    return array
#l=[0,1,5,-4,7,6,11,3]

#print(selectionSort(l))