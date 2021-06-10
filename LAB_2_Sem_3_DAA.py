from Algorithms import QuickSort_recursion as q
from Algorithms import MergeSortRecursive as m
from Algorithms import quickSortIterative as qi
from Algorithms import MergeSortIteration as mi

import psutil
import sys
import random
import time
import matplotlib.pyplot as graph

# def memoryPrint():
#     a = psutil.cpu_percent()  # cpu usage
#
#     vir_memory = psutil.virtual_memory().percent  # for ram usage
#
#     free_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
#     print()
#     print("CPU PERCENT:",a)
#     print("Virtual Memory:",vir_memory)
#     print("Free Memory:",free_memory)

sys.setrecursionlimit(1000000)

arrays=[10,100] #GIVEN LENGTHS

#QUICK SORT ITERATIVE BLUE
quick=[]
for length in arrays:
    # memoryPrint()
    #randomArray=[random.randrange(length) for _ in range(length)] #GIVEN LENGTH
    randomArray = [random.randrange(length) for _ in range(int(input()))] #CUSTOM LENGTH:
    start=time.time()
    qi.quickSortIterative(randomArray,0,len(randomArray)-1)
    finish=time.time()
    quick.append(finish-start)
    print("Quick Sort Iterative", length, finish - start)
    # memoryPrint()
# graph.plot(arrays,quick)
print()
merge=[]


#MERGE SORT RECURSIVE ORANGE
for length in arrays:
    #randomArray=[random.randrange(length) for _ in range(length)] #GIVEN LENGTH
    randomArray = [random.randrange(length) for _ in range(int(input()))] # CUSTOM LENGTH:
    start=time.time()
    randomArray=m.mergeSortRecurSive(randomArray)
    print(randomArray)
    finish=time.time()
    merge.append(finish-start)
    print("Merge Sort Recursive",length, finish-start)
graph.plot(arrays,merge)
print()

#QUICK SORT RECURSIVE
quick=[]
for length in arrays:
    #randomArray=[random.randrange(length) for _ in range(length)] #GIVEN LENGTH
    randomArray = [random.randrange(length) for _ in range(int(input()))] # CUSTOM LENGTH:
    start=time.time()
    q.quickSort(randomArray,0,len(randomArray)-1)
    finish=time.time()
    quick.append(finish-start)
    print("Quick Sort Recursive", length, finish - start)
graph.plot(arrays,quick)
print()

#MERGE SORT ITERATIVE
merge=[]
for length in arrays:
    # memoryPrint()
    #randomArray=[random.randrange(length) for _ in range(length)] #GIVEN LENGTH
    randomArray = [random.randrange(length) for _ in range(int(input()))] # CUSTOM LENGTH:
    start=time.time()
    mi.mergeSortIterative(randomArray)
    finish=time.time()
    merge.append(finish-start)
    print("Merge Sort Iterative",length, finish-start)
graph.plot(arrays,merge)

graph.show()

print()
####MEMORY ANALYSIS (ANALYSED INDIVIDUALLY FOR DIFFERENT ALGORITHMS)###