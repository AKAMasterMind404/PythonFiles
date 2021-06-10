def rotateArray(arr: list, num: int) -> list:
    for i in range(num):
        arr = arr[1::] + [arr[0]]
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    arr = rotateArray(arr, 3)

    print(arr)
