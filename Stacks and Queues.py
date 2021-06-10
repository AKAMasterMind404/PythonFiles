import numpy

class employee:
    def __init__(self,EmployeeID,EName,Phone,Age,Gender,Dep,Salary):
        self.EmployeeId=EmployeeID
        self.EName=EName
        self.Phone=Phone
        self.Age=Age
        self.Gender=Gender
        self.Dep=Dep
        self.Salary=Salary
        def printinfo():
            print(self.EmployeeId,type(self.EmployeeId))
            print(self.EName,type(self.EName))
            print(self.Phone,type(self.Phone))
            print(self.Age,type(self.Age))
            print(self.Gender,type(self.Gender))
            print(self.Salary,type(self.Salary))
            print(self.Dep,type(self.Dep))
        printinfo()

a1=employee(1001,'Atharv',99999999999,18,'Male','CEO',1000000000)
a2=employee(1002,'Sourabh',89999999999,19,'Male','Management',100000000)
a3=employee(1003,'Deep',99999999998,18,'Male','Supplies',7000000000)
a4=employee(1004,'Yash',96699999998,18,'Male','Maintanence',70000000)
a5=employee(1005,'Tejas',99990999998,18,'Male','Clerk',70000)
a6=employee(1006,'Krrish',99999987998,18,'Male','Supplies',980000000)
a7=employee(1007,'Vedant',99999999008,18,'Male','Meme Department',69)
a8=employee(1008,'Raj',99999990087,18,'Male','Office',20000000)
a9=employee(1009,'Sarah',69999999008,18,'Female','Accounts',79898787878)
a10=employee(1010,'Gauri',99999999022,18,'Female','Berojgar',999)

print(a1)

array=[None,None,None,None,None,None,None,None,None,None]
print('This array',array)
data=['a','b','c','d','e','f','g','h','i','j']
def push(array,data):
    top=-1
    z=-1
    for i in data:
        top += 1
        z += 1
        array[top]=data[z]

push(array,data)
print('This array',array)