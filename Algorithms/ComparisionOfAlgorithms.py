from Algorithms import MergeSortRecursive as ms
from Algorithms import BubbleSort as b
from Algorithms import QuickSort_recursion as q
from Algorithms import SelectionSort as s
from Algorithms import insertionSort as i
from SortingAlgorithm import SortingData as myalgorithm
from SortingAlgorithm import Efficient as e
import matplotlib.pyplot as m
import time
import random
import sys

sys.setrecursionlimit(1000000)
typelist=[e.aSort]#,i.insertionSort,b.bubbleSort,ms.mergeSort,q.quickSort,s.selectionSort,myalgorithm.sort]

for typesort in typelist:
    arrlist=[10, 100, 1000, 10000, 100000]

    axes=[]

    for num in arrlist:
        res = [random.randrange(1,101) for i in range(num)]
        start=time.time()

        if typesort!=q.quickSort:
            res=typesort(res)
        else:
            typesort(res,0,len(res)-1)
        print(res)
        finish=time.time()

        delay=(finish-start)
        print(num,delay)
        axes.append(delay)
    m.plot(arrlist,axes)
    print(str(typesort))

m.show()