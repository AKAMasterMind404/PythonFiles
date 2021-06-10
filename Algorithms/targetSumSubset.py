def targetSubsetFinder(array, num):

    if len(array) == 0:
        if num == 0:
            yield []
        return []

    if num<0:
        return []

    for solution in targetSubsetFinder(array[1:], num):
        yield solution
    for solution in targetSubsetFinder(array[1:], num - array[0]):
        yield [array[0]] + solution

if __name__=="__main__":

    target=30
    # target = int(input("Target:")) #FOR CUSTOM INPUT

    arr=[5, 10, 12, 13, 15, 18]
    # arr=list(map(int,input("Custom list:").split())) #FOR CUSTOM INPUT

    ans=[i for i in targetSubsetFinder(arr,target)]
    print(ans)