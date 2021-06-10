from DataStructures import Undirected_GRAPH as g, Array___Stack_and_Queue as a

g1=g.Graph()
g1.addNode(0,0)
g1.addNode(1,None)
g1.addNode(2,None)
g1.addNode(3,None)
g1.addNode(4,None)
g1.addNode(5,None)
g1.addNode(6,None)

g1.addToNode(0,4,3)
g1.addToNode(0,5,1)
g1.addToNode(1,5,0)
g1.addToNode(1,2,3)
g1.addToNode(1,8,2)
g1.addToNode(1,12,6)
g1.addToNode(1,3,5)
g1.addToNode(2,7,3)
g1.addToNode(2,4,4)
g1.addToNode(2,8,1)
g1.addToNode(2,5,5)
g1.addToNode(3,4,0)
g1.addToNode(3,2,1)
g1.addToNode(3,7,2)
g1.addToNode(3,3,4)
g1.addToNode(4,3,3)
g1.addToNode(4,4,2)
g1.addToNode(4,2,6)
g1.addToNode(5,3,1)
g1.addToNode(5,5,2)
g1.addToNode(6,12,1)
g1.addToNode(6,2,4)

queue=a.Array(g1.nodes).getArray()
traversedList=[]
def bfsTraverse(queue,emptylist):
    traversedList=emptylist
    for i in queue:
        if i.active==True:
            traversedList.append(i.value)
            i.active=False
        for j in i.linkedNodes.returnValuesList():
            childnode=j[0]
            if childnode.active==False:
                continue
            else:
                e=g1.searchNode(childnode.value)
                e.active=False
                traversedList.append(e.value)
                break
    return traversedList
print(g1.bfsTraverse())