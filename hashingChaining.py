class LinkedList:
    def __init__(self,h,index):
        self.head=h
        self.index=index
    def add(self,element):
        e=Element(None,element,None)
        if self.head==None:
            self.head=e
        else:
            e.prev=self.head
            self.head.next=e
            self.head=e
    def printer(self):
        x=self.head
        while x!=None:
            print(x.key)
            x=x.prev
class Element:
    def __init__(self,prev,key,next):
        self.prev=prev
        self.key=key
        self.next=next
def search(indx):
    for i in link:
        if i.index==indx:
            return i
def rev(l):
    z=len(l)-1
    c=[]
    while z>=0:
        c.append(l[z])
        z-=1
    return c

d={'Alex':113456,'John':462,'Nick':488,'Ken':498,'Justin':455,
   'Valerie':459,'Brenda':476,'June':452,'April':477,
   'Chris':193443,'James':213421,'Lily':513311}

temp={}
prn=int(input('Enter the last 4 digits of your PRN:'))
prn=int('2019080'+str(prn))
for l in d:
    if l not in ['Alex','Chris','James','Lily']:
        temp[l]=int(str(prn)+str(d.get(l)))
    else:
        temp[l]=d.get(l)
d=temp
link=[]
z=0
print()
print('Calculations for PRN',prn,':')
print(d)
print()
for i in d:
    link.append(LinkedList(None,z))
    z+=1
for j in d:
    t=0
    print('ASCII(',j,')','=',)
    for k in j:
        f=ord(k)
        t+=f
        print(f,end='+')
    print(t)
    s=0
    for i in str(d.get(j)):
        s+=int(i)
    index=(t+s)%11
    print(j,'[',str(d.get(j)),']:(',t,'+',s,')%11 =',index)
    obj=search(index)
    obj.add(j)
print()
print('Hash Table for PRN',prn,'as follows:')
print()
for i in link:
    x=i.head
    if x==None:
        print(i.index,x)
    else:
        fin=[]
        while x!=None:
            fin.append(x.key)
            x=x.prev
        fin=rev(fin)
        for j in fin:
            print(i.index,j,end=' ')
        print()