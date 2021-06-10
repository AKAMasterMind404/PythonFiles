#COPYRIGHT:::::::::ATHARV KARBHARI BTech CSE
class student:
    def __init__(self,prn,name,age,gender,email,grade):
        self.prn=int(prn)
        self.name=name
        self.age=int(age)
        self.gender=gender
        self.email=email
        self.grade=grade
    def printinfo(self):
        print(self.prn)
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.email)
        print(self.grade)
        print()
object1=student(20190802001,'Atharv',18,'male','email','A')
object2=student(20190802002,'Btharv',28,'male','email','A')
object3=student(20190802003,'Ctharv',38,'male','email','A')
object4=student(20190802004,'Dtharv',48,'male','email','A')
object5=student(20190802005,'Etharv',68,'male','email','A')
object6=student(20190802006,'Ftharv',18,'male','email','A')
object7=student(20190802007,'Gtharv',78,'male','email','A')
object8=student(20190802008,'Htharv',88,'male','email','A')
object9=student(20190802009,'Itharv',98,'male','email','A')
object10=student(20190802010,'Jtharv',108,'male','email','A')

class element:
    def __init__(self,prev,value,next):
        self.prev=prev
        self.value=value
        self.next=next
class linkedlist:
    def __init__(self,head):
        self.head=head
        self.start=None
    def insert(self,value):
        e=element(None,value,None)
        if self.head==None:
            self.head=e
            self.start=e
        else:
            e.prev=self.head
            self.head.next=e
            self.head=e
    def printer(self):
        li=[]
        def p(x):
            if x!=None:
                li.append(x.value)
                p(x.prev)
        p(self.head)
        z=len(li)-1
        while z>=0:
            print(li[z].prn)
            z-=1
    def print2(self):
        x=self.start
        while x!=None:
            print(x.value.prn)
            x=x.next
    def delete(self, x):
        a = l1.search(x)
        if a.prev==None:
            a.next.prev=None
            l1.printer()
        elif a.next==None:
            a.prev.next=None
            l1.printer()
        else:
            a.prev.next=a.next
            a.next.prev=a.prev
            l1.printer()
    def search(self,svalue):
            v = []
            def f(x):
                if x.value.prn==svalue:
                    print('Previous:',x.prev.value.prn)
                    print('Your Value:',x.value.prn)
                    v.append(x)
                    try:
                        print('Next:',x.next.value.prn)
                    except AttributeError:
                        print('Next:Does not exist/Not Inserted')
                else:
                    f(x.prev)
            try:
                f(self.head)
            except IndexError:
                print('Key Not Found!')
            return v[0]

l1=linkedlist(None)
x=True
oblist=[object1,object2,object3,object4,object5,object6,object7,object8,object9,object10]
while x==True:
    print('1.For Insertion')
    print('2.For Searching')
    print('3.For Iteration')
    print('4.For Deletion')
    print('5.To exit')
    ans=int(input('Type here:'))
    if ans==1:
        for i in oblist:
            print('Do you want to insert object?[Y/N]')
            j=input().lower()
            if j=='y':
                l1.insert(i)
                l1.printer()
            elif j=='n':
                break
    elif ans==2:
        ask=int(input('Search for prn here:'))
        k=l1.search(ask)
    elif ans==3:
        l1.print2()
    elif ans==4:
        print('Enter PRN to delete:')
        op=int(input())
        l1.delete(op)
    elif ans==5:
        x=False

