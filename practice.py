import numpy as n

array1=n.array([None,None,None,None,None,None,None,None,None,None])
head=0
tail=0

def push(tail,array,object):
    if tail<len(array):
        array[tail]=object
        tail+=1
        return tail,array
    else:
        print('Overflow bastard!')

(tail,array1)=push(tail,array1,'oho')
(tail,array1)=push(tail,array1,'oh1')
(tail,array1)=push(tail,array1,'oh2')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')
(tail,array1)=push(tail,array1,'oh3')


print(tail,array1)