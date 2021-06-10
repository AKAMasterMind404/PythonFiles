from collections import namedtuple

students=int(input())

fields=input().split()

StudentData=namedtuple('StudentList','{},{},{},{}'.format(fields[0],fields[1],fields[2],fields[3]))

tupleList=[]

sum1=0

for i in range(students):
    data=input().split()
    st1=StudentData(data[0],data[1],data[2],data[3])
    sum1+=int(st1.MARKS)

average=sum1/students
if float(average)!=int(average):
    a=float(str(average)[0:5])
print(average)