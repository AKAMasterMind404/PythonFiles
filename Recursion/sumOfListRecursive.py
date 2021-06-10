def sumOfList(arr):
    total=0
    if len(arr)==1:
        total+=arr[-1]
        return total
    else:
        print("array",arr)
        print("element",arr[-1])
        return arr[-1]+sumOfList(arr[0:-1:])

if __name__=="__main__":
    print(sumOfList([1,2,3]))