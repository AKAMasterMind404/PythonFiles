#GIVEN AN ARRAY OF N+1 INTEGERS WHERE WEACH INTEGER IS BETWEEN 1 TO N INCLUSIVE. Prove that atleast one duplicate must exitss
arr=[3,4,1,0,6,9]

def bubbleSort(arr):
    l = len(arr)
    p1 = 0
    p2 = 1
    for i in range(0,l):
        while p1<l-1:
            if arr[p1]>arr[p2]:
                arr[p1],arr[p2]=arr[p2],arr[p1]
            #print(p1,p2)
            p1+=1
            p2+=1
        p1=0
        p2=1
    return arr

#print(bubbleSort(arr))