def minimumSwaps(arr):
    sortedarray=sorted(arr)
    def swap( a, b):
        a1 = arr[a]
        b1 = arr[b]
        arr[a] = b1
        arr[b] = a1
        return arr
    nos=0
    for i in sortedarray:
        s=sortedarray.index(i)
        a=arr.index(i)
        if s!=a:
            arr=swap(s,a)
            nos+=1
    return nos