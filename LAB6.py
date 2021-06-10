#PRN: 20190802003 NAME: ATHARV KARBHARI

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def edge(self, u, v):
        self.graph[u].append(v)
    def DFS(self, v, visited):
        visited[v] = True
        global t
        print(v, end=' ')
        pr[v] = t
        t += 1
        check.append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)
    def BFS(self, s):
        visited = [False] * (max(self.graph)+1)
        queue = []
        global a
        a=[]
        queue.append(s)
        a.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    a.append(i)
                    visited[i] = True

if __name__=='__main__':

    g=Graph()

    g.edge(1, 2)
    g.edge(2, 1)
    g.edge(1, 3)
    g.edge(3, 1)
    g.edge(2, 4)
    g.edge(4, 2)
    g.edge(3, 4)
    g.edge(4, 3)
    g.edge(3, 5)
    g.edge(5, 3)
    g.edge(5, 6)
    g.edge(6, 5)

    visited = [False] * (max(g.graph)+1)
    t=1
    pr={}
    po={}
    check=[]
    a=[]
    print("1)DFS inorder:")
    g.DFS(1,visited)
    print()
    print("BFS inorder:")
    g.BFS(1)
    print()
    print("2)Checking all vertices for strong connection")
    x=g.graph[max(g.graph)]

    for i in g.graph:
        c=sorted(a)
        g.BFS(i)
        print()
        if(c==sorted(a)):
            strong=True
        else:
            strong=False
            break

    if(strong):
        print("Graph is Strongly Connected")
    else:
        print("Graph is not Strongly Connected")
    print("DFS pre/post visit times:")
    for i in check[::-1]:
        po[i]=int(t)
        t+=1
    for i in pr:
        print("Node",i,":- Pre:",pr[i]," Post:",po[i],)