class student:
    global pnr,student_name,email,age,gender,grade
    def __init__(self):
        self.pnr=int(input("\nEnter  PRN:-"))
        self.student_name=input("\nEnter Student Name:-")
        self.email=input("\nEnter Email:-")
        self.age=int(input("\nEnter Age:-"))
        self.gender=input("\nEnter Gender(M/F):-")
        self.grade=input("\nEnter Grade:-")
    def printinfo(self):
        print(self.pnr,self.student_name,self.email,self.age,self.gender,self.grade)
res1=student()
res2=student()
res3=student()
res4=student()
res5=student()
res6=student()
res7=student()
res8=student()
res9=student()
res10=student()
lis=[res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]

#CREATION OF DOUBLY LINKED LIST
class Element():
   def __init__(self,key,pred,succ):
       self.key = key
       self.pred = pred
       self.succ = succ
class myList():
   def __init__(self,head,tail):
        self.head = head
        self.tail = tail

   def insert(self, value):
       element = Element(value, None, None)
       # the new element will become the head
       if self.head == None:
            self.head = element
            self.head.succ=self.head.pred=element
            self.tail=self.head
       elif self.head==self.tail :
           self.head.pred=element
           element.succ=self.head
           self.head.succ = element
           element.pred = self.head
           self.tail=element


       else:
           self.head.pred=element
           element.succ=self.head
           element.pred=self.tail
           self.tail.succ=element
           self.tail=element

   def printElements(self):
       x = self.head
       if (x==None):
           print("LIST EMPTY")
       else:
            while (x.succ!=self.head):
                (x.key.printinfo(), ",")
                x = x.succ
            x.key.printinfo()
   def search(self, searchValue):
        var = self.head
        if (var==None):
            print("LIST EMPTY")
        else:
            while var != None and var.key != searchValue:
                var = var.pred
                if var==self.head:
                    break
            var.key.printinfo()

            return var
   def delete(self, x):
        a=theList.search(x)
        if a==self.head:
            self.tail.succ=self.head.succ
            self.head.succ.pred=self.tail
            self.head=self.head.succ
        elif a==self.tail:
            self.tail.pred.succ = self.head
            self.head.pred = self.tail.pred
            self.tail = self.tail.pred
        else:
            a.pred.succ=a.succ
            a.succ.pred=a.pred

theList = myList(None,None)
i=0
choice=True
while choice:
    print("\n1-insert\n2-delete\n3-search\n4-iterate\n5-exit\n")
    ans=int(input())
    if ans==1:
        for j in range(0,len(lis)):
            theList.insert(lis[i])
            i=i+1
        theList.printElements()
    elif ans==2:
        ab=int(input("Enter Prn"))
        if ab>=11:
            print("invalid Prn")
        else:
            theList.delete(lis[ab-1])
            theList.printElements()
    elif ans==3:
        ab = int(input("Enter Prn"))
        if ab<11:
            try:
                a=theList.search(lis[ab-1])
                if a==0:
                    a.key.printinfo()
            except Exception:        
                print("No Entry")    
               
        else:
            print("invalid Prn")
    elif ans==4:
        theList.printElements()
    else:
        print("Wrong Operation")
        break

    ch=input("Do You Want to continue(Y/N):-")
    if ch=='y' or ch=='Y':
        choice=True
    else:
        choice=False    