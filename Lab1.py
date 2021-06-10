import numpy as n

class employee:
    def __init__(self,ID,Name,Age,Phone,Gender,dep,sal):
        self.id1=int(ID)
        self.name=str(Name)
        self.age=int(Age)
        self.phone=int(Phone)
        self.gender=str(Gender)
        self.dep=str(dep)
        self.salary=int(sal)
    def printinfo(self):
        print('Employee ID is:',self.id1)
        print('Employee Name is:',self.name)
        print('Employee Age is:',self.age)
        print('Employee phone is:', self.phone)
        print('Employee gender is:', self.gender)
        print('Employee department is:', self.dep)
        print('Employee salary is:', self.salary)
        print()
#Q1
obj1=employee(1001,'Atharv',18,8989898900,'Male','Acoounts',999999)
obj2=employee(1002,'BCD',18,99989899832,'Male','Marketing',180000)
obj3=employee(1003,'Deep',99999999998,18,'Male','Supplies',7000000000)
obj4=employee(1004,'Yash',96699999998,18,'Male','Maintanence',70000000)
obj5=employee(1005,'Tejas',99990999998,18,'Male','Clerk',70000)
obj6=employee(1006,'Krrish',99999987998,18,'Male','Supplies',980000000)
obj7=employee(1007,'Vedant',99999999008,18,'Male','Meme Department',69)
obj8=employee(1008,'Raj',99999990087,18,'Male','Office',20000000)
obj9=employee(1009,'Sarah',69999999008,18,'Female','Accounts',79898787878)
obj10=employee(1010,'Gauri',99999999022,18,'Female','Peon',999)

#Q2
print(obj1)
print(obj2)
print(obj3)
print(obj4)
print(obj5)
print(obj6)
print(obj7)
print(obj8)
print(obj9)
print(obj10)

#Q3

employeearray=n.array([None,None,None,None,None,None,None,None,None,None])

l=len(employeearray)
z=0

employeearray[0]=obj1
employeearray[1]=obj2
employeearray[2]=obj3
employeearray[3]=obj4
employeearray[4]=obj5
employeearray[5]=obj6
employeearray[6]=obj7
employeearray[7]=obj8
employeearray[8]=obj9
employeearray[9]=obj10

print(employeearray)

#Q4
for i in employeearray:
    i.printinfo()
    print(i.id1)

#Q5
def deleteask(employeearray):
    i=input('Do you want to delete some records?(Y/N)')
    i=i.lower()
    if i=='y':
        j=int(input('Enter the ID you want to delete:'))
        for k in employeearray:
            if k.id1==j:
                confirm=input('This ID exists.Proceed with deletion?(Y/N)')
                confirm=confirm.lower()
                if confirm=='y':
                    possibledel = k
                    new=[]
                    for i in employeearray:
                        if i!=possibledel:
                            new.append(i)
                    employeearray=new
                    return employeearray


print(deleteask(employeearray))