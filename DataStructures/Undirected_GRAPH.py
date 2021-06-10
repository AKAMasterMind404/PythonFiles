from DataStructures import LinkedList as l
class Node:
    def __init__(self,value,linkedNodes):
        self.value=value
        self.linkedNodes=linkedNodes
        # self.distValue=dist
        self.active=True
class Graph:
    def __init__(self):
        self.nodes=[]
        self.nodevalues=[]
    def addNode(self,nodevalue):
        if nodevalue not in self.nodevalues:
            linkedlist=l.linkedList()
            node=Node(nodevalue,linkedlist)
            self.nodes.append(node)
            self.nodevalues.append(nodevalue)
        else:
            print('Node with this value exists!')
    def addToNode(self,parent,distFromChild,child):
        parent=self.searchNode(parent)
        child=self.searchNode(child)
        if parent and child and child not in parent.linkedNodes.returnList():
            parent.linkedNodes.insert((child,distFromChild))
            child.linkedNodes.insert((parent,distFromChild))
        else:
            print('Could not complete action:Parent/Child node has not been initialised or has already been initialised.')
    def searchNode(self,value):
        for i in self.nodes:
            if i.value==value:
                return i
    def deleteNode(self,value):
        node=self.searchNode(value)
        if node==None:
            print('Node does not exist!')
        else:
            self.nodevalues.remove(value)
            self.nodes.remove(node)
    def printGraph(self):
        print("######################")
        for i in self.nodes:
            val=[]
            for j in i.linkedNodes.returnValuesList():
                val.append((j[0].value,j[1]))
            print(i.value, val)
            # print(i.value,i.distValue,val)
        print("######################")
    def bfsTraverse(self):
        queue=self.nodes
        traversedList =[]
        for i in queue:
            if i.active == True:
                traversedList.append(i.value)
                i.active = False
            for j in i.linkedNodes.returnValuesList():
                childnode = j[0]
                if childnode.active == False:
                    continue
                else:
                    e = self.searchNode(childnode.value)
                    e.active = False
                    traversedList.append(e.value)
                    break
        return traversedList

if __name__=='__main__':
    b1=Graph()
    b1.addNode('A')
    b1.addNode('B')
    b1.addNode('C')
    b1.addNode('D')
    b1.addNode('E')
    b1.addNode('F')
    b1.addNode('G')
    b1.addNode('H')
    b1.addToNode('A',1,'B')
    b1.addToNode('A',1,'C')
    b1.printGraph()
    print(b1.searchNode('A').linkedNodes.returnValuesList())