import numpy as n

class student:
    def __init__(self,prn,sn,em,a,g,per):
        self.prn=prn
        self.name=sn
        self.email=em
        self.age=a
        self.gender=g
        self.percentage=per
    def printinfo(self):
        print(self.prn)
        print(self.name)
        print(self.email)
        print(self.age)
        print(self.gender)
        print(self.percentage)
        print()

def Enqueue(top,array,object):
    if top>=0:
        if object not in array:
            array[top]=object
            top-=1
        else:
            print('Duplicate Entry! Could not add item')
    else:
        print('Overflow')
    return top,array

def Dequeue(top,array):
    res=0
    if top>=0:
        if array[top]==None:
            (top,array,res)=Dequeue(top-1,array)
        else:
            array[top]=None
            top-=1
    else:
        print('underflow!')
        res=1
    return top,array,res

array1=n.array([None,None,None,None,None,None,None,None,None,None])
top1=0

o1=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o2=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o3=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o4=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o5=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o6=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o7=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o8=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o9=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o10=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)
o11=student(20190802005,'ABC','vedant@gmail.com',18,'Male',91)

objectlist=[o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11]

for i in objectlist:
    i.printinfo()

top2=len(array1)-1
print(top2)

for i in objectlist:
    imp=input('Do you want to enqueue the element?(Y/N)')
    if imp=='y':
        (top2,array1)=Enqueue(top2,array1,i)
        print('The following record has been enqueued:')
        i.printinfo()
        print(array1)
    else:
        break
print(array1)

top=len(array1)-1
for i in range(1,99):
    imp=input('Do you want to dequeue?(Y/N)')
    if imp.lower()=='y':
        (top,array1,res)=Dequeue(top,array1)
        print('Dequeued!')
    else:
        break

print(array1)