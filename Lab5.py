# COPYRIGHT:::::::::ATHARV KARBHARI BTech CSE

class student:
    def __init__(self, prn, name, age, gender, email, grade):
        self.prn = int(prn)
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.email = email
        self.grade = grade
    def printinfo(self):
        print(self.prn)
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.email)
        print(self.grade)
        print()

object1 = student(20190802001, 'Atharv', 18, 'male', 'email', 'A')
object2 = student(20190802002, 'Btharv', 28, 'male', 'email', 'A')
object3 = student(20190802003, 'Ctharv', 38, 'male', 'email', 'A')
object4 = student(20190802004, 'Dtharv', 48, 'male', 'email', 'A')
object5 = student(20190802005, 'Etharv', 68, 'male', 'email', 'A')
object6 = student(20190802006, 'Ftharv', 18, 'male', 'email', 'A')
object7 = student(20190802007, 'Gtharv', 78, 'male', 'email', 'A')
object8 = student(20190802008, 'Htharv', 88, 'male', 'email', 'A')
object9 = student(20190802009, 'Itharv', 98, 'male', 'email', 'A')
object10 = student(20190802010, 'Jtharv', 108, 'male', 'email', 'A')
oblist=[object1,object2,object3,object4,object5,object6,object7,object8,object9,object10]
class Node:
    def __init__(self,key,parent,left,right):
        self.key=key
        self.parent=parent
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self,root):
        self.root=root
    def insertNew(self,value):
        node=Node(value,None,None,None)
        if self.root==None:
            self.root=node
        else:
            x=self.root
            while True:
                if value.prn<x.key.prn and x.left==None:
                    node.parent=x
                    x.left=node
                    break
                elif value.prn<x.key.prn and x.left!=None:
                    x=x.left
                elif value.prn>x.key.prn and x.right==None:
                    node.parent=x
                    x.right=node
                    break
                elif value.prn>x.key.prn and x.right!=None:
                    x=x.right
    def search(self,value):
        x=self.root
        while True:
            try:
                if value>x.key.prn:
                    x=x.right
                elif value<x.key.prn:
                    x=x.left
                elif value==x.key.prn:
                    return x
            except AttributeError:
                print('PRN NOT FOUND!')
                break

    def printTree(self):
        def nonecheck(list1):
            z = 0
            for i in list1:
                if i == None:
                    z += 1
            if len(list1) == z:
                return 1
            else:
                return 0
        x = self.root
        l = [x]
        final=[x.key.prn]
        print(x.key.prn)
        while True:
            inlist = []
            nc = nonecheck(l)
            if nc == 0:
                temp = []
                for i in l:
                    try:
                        print(i.left.key.prn,end=' ')
                        final.append(i.left.key.prn)
                        inlist.append(i.left)
                    except AttributeError:
                        print(None, end=' ')
                        final.append(None)
                        inlist.append(None)
                    try:
                        print(i.right.key.prn, end=' ')
                        final.append(i.right.key.prn)
                        inlist.append(i.right)
                    except AttributeError:
                        print(None, end=' ')
                        final.append(None)
                        inlist.append(None)
                    l = inlist
                print()
            else:
                break
        #final contains listed values

bt1=BinarySearchTree(None)
#Insertion
while True:
    print('1.Insertion(Mandatory)')
    print('2.Searching')
    print('3.Printing the tree')
    print('4.Exit')
    inp=int(input('Choose an action:'))
    if inp==1:
        for i in oblist:
            j=input('Do you want to insert object?(Y/N):')
            if j.lower()=='y':
                bt1.insertNew(i)
    elif inp==2:
    #search
        j=int(input('Enter a prn to search:'))
        try:
            bt1.search(j).key.printinfo()
        except AttributeError:
            print('Error:PRN does not exist!')
    elif inp==3:
        bt1.printTree()
    elif inp==4:
        break
    else:
        print('Invalid input!')
