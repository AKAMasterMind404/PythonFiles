import numpy as n

array2=n.array([None,None,None,None,None])
top1=0
top2=len(array2)-1

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

def StackPop(top,array):
    if top<len(array):
        if array[top]==None:
            (top,array)=StackPop(top+1,array)
        else:
            array[top]=None
    else:
        print('Underflow!')
    return top,array


(top2,array2)=push(top2,array2,'Hi')
(top2,array2)=push(top2,array2,'OP')
(top2,array2)=push(top2,array2,'H1')
(top2,array2)=push(top2,array2,'ii')
(top2,array2)=push(top2,array2,'1')

(top1,array2)=StackPop(top1,array2)
(top1,array2)=StackPop(top1,array2)
(top1,array2)=StackPop(top1,array2)
(top1,array2)=StackPop(top1,array2)
(top1,array2)=StackPop(top1,array2)
(top1,array2)=StackPop(top1,array2)

print(array2)