def binarySearch(l, h, arr, element):
    if element > arr[-1]:
        return element
    if l > h:
        return l
    
    mid = l + (h - l) // 2

    if arr[mid] == element:
        return mid
    elif arr[mid] < element:
        return binarySearch(mid + 1, h, arr, element)
    else:
        return binarySearch(l, mid - 1, arr, element)


if __name__ == "__main__":
    print(binarySearch(0, 4, [1, 3, 5, 6], 7))
