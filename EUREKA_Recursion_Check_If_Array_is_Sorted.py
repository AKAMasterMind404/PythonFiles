def isSorted(array):
    if len(array)==1:
        return True

    elif len(array):
        x=len(array)-1
        return array[x-1]<=array[x] and isSorted(array[:x])

array=[-4,0,1,2,3,4,5,6,8,56]

print(isSorted(array))