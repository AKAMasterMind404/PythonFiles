import sys
import time
import psutil

n = int(sys.argv[1])
print("The number of arguments: ", n)

import random

# Generate list of random numbers between the given argument
random_list = random.sample(range(0, n + 1), n)


def heap(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heaping
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heap(arr, i, 0)


print("the given array is: ", random_list)
start = time.time()  # start time
time.sleep(1)
heapSort(random_list)
length = len(random_list)

print("Sorted array is")
for i in range(length):
    print("%d " % random_list[i], end='')

end = time.time()

a = psutil.cpu_percent()  # cpu usage

vir_memory = psutil.virtual_memory().percent  # for ram usage

free_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

print("\nRuntime of the program is {}\n".format((end-start)-1))

print("The number of arguments: ", n)

print("{}% of CPU is used".format(a))

print("{}% MEMORY is used".format(vir_memory))

print("{}% MEMORY is free".format(free_memory))
