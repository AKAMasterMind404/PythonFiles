def colorGiver(bool):
    if bool:
        return "Red"
    else:
        return "Black"

class Node:
    def __init__(self,color,value,parent,left,right):
        self.color=color
        self.value=value
        self.parent=parent
        self.left=left
        self.right=right

class RBTree:
    def __init__(self):
        self.root=None
    def insertNode(self,val):
        if self.root==None:
            self.root=Node("Black",val,None,None,None)
        else:
            temp=Node("Red",val,None,None,None)
            x=self.root
            while True:
                if val>x.value and not x.right:
                    break
                elif val>x.value and x.right:
                    x=x.right
                if val<x.value and not x.left:
                    break
                elif val<x.value and x.left:
                    x=x.left



tree1=RBTree()
tree1.insertNode(10)
print(tree1.root.color)