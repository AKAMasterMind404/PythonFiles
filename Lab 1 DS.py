lol=[]
class employee:
    def __init__(self,EmployeeID,EName,Phone,Age,Gender,Dep,Salary):
        X=[]
        self.EmployeeId=EmployeeID
        self.EName=EName
        self.Phone=Phone
        self.Age=Age
        self.Gender=Gender
        self.Dep=Dep
        self.Salary=Salary
        print(self.EmployeeId,type(self.EmployeeId))
        print(self.EName,type(self.EName))
        print(self.Phone,type(self.Phone))
        print(self.Age,type(self.Age))
        print(self.Gender,type(self.Gender))
        print(self.Salary,type(self.Salary))
        print(self.Dep,type(self.Dep))
        X.append(self.EmployeeId)
        X.append(self.EName)
        X.append(self.Phone)
        X.append(self.Age)
        X.append(self.Gender)
        X.append(self.Dep)
        print('This is X:',X)
        lol.append(X)

employee(1001,'Atharv',99999999999,18,'Male','CEO',1000000000)
employee(1002,'Sourabh',89999999999,19,'Male','Management',100000000)
employee(1003,'Deep',99999999998,18,'Male','Supplies',7000000000)
employee(1004,'Yash',96699999998,18,'Male','Maintanence',70000000)
employee(1005,'Tejas',99990999998,18,'Male','Clerk',70000)
employee(1006,'Krrish',99999987998,18,'Male','Supplies',980000000)
employee(1007,'Vedant',99999999008,18,'Male','Meme Department',69)
employee(1008,'Raj',99999990087,18,'Male','Office',20000000)
employee(1009,'Sarah',69999999008,18,'Female','Accounts',79898787878)
employee(1010,'Gauri',99999999022,18,'Female','Peon',999)
print(lol)
array=[None,None,None,None,None,None,None,None,None,None]
print('This array',array)

def push(array,data):
    top=-1
    z=-1
    for i in data:
        top += 1
        z += 1
        array[top]=data[z]

push(array,lol)
print('This array',array)
