def isDescending(arr):
    if len(arr) == 1:
        return True
    else:
        return arr[0] > arr[1] and isDescending(arr[1::])


# arr=[6,5,8,4,7,10,9]
def poisonousPlants(p):
    num = 0
    while not isDescending(p):
        dedPlants = [i + 1 for i in range(len(p) - 1) if p[i] < p[i + 1]]

        l = [p[i] for i in range(len(p)) if i not in dedPlants]
        p = l
        num += 1
    return num


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
