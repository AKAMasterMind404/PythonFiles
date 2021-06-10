import numpy as n

def push(top,array,object):
    if top>=0:
        if object not in array:
            array[top]=object
            top-=1
        else:
            print('Duplicate Entry! Could not add item')
    else:
        print('Overflow')
    return top,array

def QueuePop(top,array):
    if top>=0:
        if array[top]==None:
            (top,array)=QueuePop(top-1,array)
        else:
            array[top]=None
            top-=1
    else:
        print('underflow!')
    return top,array

a1=3

array1=n.array([None,None,None,None,None,None])
