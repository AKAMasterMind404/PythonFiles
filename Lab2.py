import numpy as n
#Q1
class student:
    def __init__(self,prn,name,email,age,gender,percentage):
        self.prn=int(prn)
        self.name = str(name)
        self.email = str(email)
        self.age = int(age)
        self.gender = str(gender)
        self.per = int(percentage)
    def printinfo(self):
        print(self.prn,self.name,self.email,self.age,self.gender,self.per)
''''data=[]
attributes=['prn','name','email','age','gender','percentage']
for i in attributes:
    print('Enter data for ',i)
    data.append(input())
student(data[0],data[1],data[2],data[3],data[4],data[5]).printinfo()'''
#Q2
studentArray=n.array([None,None,None,None,None,None,None,None,None,None])#stack
top=-1
object1=student(20190802003,'Atharv','a@123',18,'male',89)
object2=student(20190802005,'Mnss','B@123',20,'female',9)
object3=student(20190802005,'Mnss','B@123',20,'female',9)
object4=student(20190802005,'Mnss','B@123',20,'female',9)
object5=student(20190802005,'Mnss','B@123',20,'female',9)
object6=student(20190802005,'Mnss','B@123',20,'female',9)
object7=student(20190802005,'Mnss','B@123',20,'female',9)
object8=student(20190802005,'Mnss','B@123',20,'female',9)
object9=student(20190802005,'Mnss','B@123',20,'female',9)
object10=student(20190802005,'Mnss','B@123',20,'female',9)
object11=student(20190802005,'Mnss','B@123',20,'female',9)
def push(top,array,object):
    l=len(array)
    if top==l-1:
        print('Overflow!!')
    else:
        top += 1
        array[top]=object
    return top,array
#print(top)
(top,studentArray)=push(top,studentArray,object1)
(top,studentArray)=push(top,studentArray,object2)
(top,studentArray)=push(top,studentArray,object3)
(top,studentArray)=push(top,studentArray,object4)
(top,studentArray)=push(top,studentArray,object5)
(top,studentArray)=push(top,studentArray,object6)
(top,studentArray)=push(top,studentArray,object7)
(top,studentArray)=push(top,studentArray,object8)
(top,studentArray)=push(top,studentArray,object9)
(top,studentArray)=push(top,studentArray,object10)
(top,studentArray)=push(top,studentArray,object11)
#print(top)

#Q3
for i in studentArray:
    i.printinfo()

#Q4
top=len(studentArray)-1
def pop(top,array):
    l=len(array)
    popped=None
    if top>=0:
        popped=array[top]
        array[top]=None
        top-=1
    elif top<0:
        print('Underflow')
    return popped,array,top
print(top)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
(popped,studentArray,top)=pop(top,studentArray)
print(top)

print(studentArray)