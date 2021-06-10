class employee:
    def __init__(self,i,name,email,age,gender):
        self.id = int(i)
        self.name = name
        self.email = email
        self.age = int(age)
        self.gender = gender
    def printinfo(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.gender)
        print()

class Node:
    def __init__(self,key,parent,left,right):
        self.key=key
        self.parent=parent
        self.left=left
        self.right=right
class BST:
    def __init__(self):
        self.root=None
    def insertNode(self, value):
        node = Node(value, None, None, None)
        if self.root == None:
            self.root = node
        else:
            x = self.root
            while True:
                if value < x.key and x.left == None:
                    node.parent = x
                    x.left = node
                    break
                elif value < x.key and x.left != None:
                    x = x.left
                elif value > x.key and x.right == None:
                    node.parent = x
                    x.right = node
                    break
                elif value > x.key and x.right != None:
                    x = x.right
            # while True:
            #     if value.id < x.key.id and x.left == None:
            #         node.parent = x
            #         x.left = node
            #         break
            #     elif value.id < x.key.id and x.left != None:
            #         x = x.left
            #     elif value.id > x.key.id and x.right == None:
            #         node.parent = x
            #         x.right = node
            #         break
            #     elif value.id > x.key.id and x.right != None:
            #         x = x.right
    def search(self, value):
                x = self.root
                while True:
                    try:
                        if value > x.key.id:
                            x = x.right
                        elif value < x.key.id:
                            x = x.left
                        else:
                            return x
                    except AttributeError:
                        print('PRN NOT FOUND!')
                        break
    def deleteLeafNode(self,id):
        c=self.search(id)
        if c.left==None and c.right==None:
            if c.parent.left==c:
                c.parent.left=None
                c.parent=None
            elif c.parent.right==c:
                c.parent.right=None
                c.parent=None
            print('ID has been deleted!')
        else:
            print('Deletion cannot be made!Specified selection is not a leaf node!')
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
        final=[x.key]
        print(x.key)
        # final=[x.key.id]
        # print(x.key.id)
        while True:
            inlist = []
            nc = nonecheck(l)
            if nc == 0:
                temp = []
                for i in l:
                    try:
                        print(i.left.key,end=' ')
                        # print(i.left.key.id,end=' ')
                        # final.append(i.left.key.id)
                        final.append(i.left.key)
                        inlist.append(i.left)
                    except AttributeError:
                        print(None, end=' ')
                        final.append(None)
                        inlist.append(None)
                    try:
                        print(i.right.key, end=' ')
                        # print(i.right.key.id, end=' ')
                        # final.append(i.right.key.id)
                        final.append(i.right.key)
                        inlist.append(i.right)
                    except AttributeError:
                        print(None, end=' ')
                        final.append(None)
                        inlist.append(None)
                    l = inlist
                print()
            else:
                break

if __name__=='__main__':
    object1 = employee(15, 'Abc', 'email', 18, 'Male')
    object2 = employee(12, 'Abc', 'email', 18, 'Male')
    object3 = employee(33, 'Abc', 'email', 18, 'Male')
    object4 = employee(14, 'Abc', 'email', 18, 'Male')
    object5 = employee(16, 'Abc', 'email', 18, 'Male')
    object6 = employee(66, 'Abc', 'email', 18, 'Male')
    object7 = employee(76, 'Abc', 'email', 18, 'Male')
    object8 = employee(18, 'Abc', 'email', 18, 'Male')
    object9 = employee(9, 'Abc', 'email', 18, 'Male')
    object10 = employee(10, 'Abc', 'email', 18, 'Male')

    oblist = [object1, object2, object3, object4, object5, object6, object7, object8, object9, object10]
    bt1=BST()
    while True:
        print('1.Insertion(Mandatory)')
        print('2.Searching')
        print('3.Printing the tree')
        print('4.Delete a leaf node')
        print('5.Exit')
        inp=int(input('Choose an action:'))
        if inp==1:
            for i in oblist:
                j=input('Do you want to insert object?(Y/N):')
                if j.lower()=='y':
                    bt1.insertNode(i)
        elif inp==2:
        #search
            j=int(input('Enter an ID to search:'))
            try:
                bt1.search(j).key.printinfo()
            except AttributeError:
                print('Error:PRN does not exist!')
        elif inp==3:
            bt1.printTree()
        elif inp==4:
            ip=int(input('Enter an ID to delete:'))
            bt1.deleteLeafNode(ip)
        elif inp==5:
            break
        else:
            print('Invalid input!')