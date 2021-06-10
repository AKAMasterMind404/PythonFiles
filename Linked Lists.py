class student:
    def __init__(self,prn,sn,email,age,gender,grade):
        self.prn=prn
        self.name=sn
        self.email=email
        self.age=age
        self.gender=gender
        self.grade=grade
    def printinfo(self):
        print(self.prn)
        print(self.name)
        print(self.email)
        print(self.age)
        print(self.gender)
        print(self.grade)

class Element:
    def __init__(self,key,pred,succ):
        self.pred=pred
        self.key=key
        self.succ=succ
class Mylist:
    def __init__(self,head):
        self.head=head
    def insert(self,x):
        e = Element(x, None, None)
        if self.head==None:
            self.head=e
        else:
            self.head.succ=e
        e.pred=self.head
        self.head=e
    def search(self,s):
        v=self.head
        while v!=None and v.key!=s:
            v=v.pred
            return v
    def printElement(self):
        x=self.head
        if x==None:
            print(x)
        while x!=None:
            print(x.key)
            x=x.pred

l1=Mylist(None)
l1.insert(10)
l1.printElement()