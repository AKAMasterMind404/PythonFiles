import random
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr
#MY CODE:
# def insertionSort(array):
#     array=[i for i in array]
#     i=0
#     while i<len(array)-1:
#         z=i-1
#         inferior=array[i]
#         while inferior<array[z]:
#             if z>0:
#                 z-=1
#             else:
#                 break
#         x=array.pop(i)
#         array.insert(z+1,x)
#         i+=1
#     print(array)
# l1=[random.randrange(1,20) for i in range(0,10)]