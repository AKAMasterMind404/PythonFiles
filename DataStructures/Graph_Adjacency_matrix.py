# Undirected Graph
class Graph:
    def __init__(self):
        self.nodes = {}  # {'A':0,'B':1,'C':2,'D':3,'E':4}
        self.graph = []  # graph=[[0,1,0,0,0],[],[],[],[]]
        self.init = 0

    def printChildren(self):
        for i in self.getNodes():
            print(i, ':', self.getChildren(i))

    def getNodes(self):
        return list(self.nodes.keys())

    def addNodes(self, *i):
        for n in i:
            self.nodes[n] = self.init
            self.init += 1
        if not len(self.graph):
            for j in i:
                self.graph.append([0] * len(i))
        else:
            extra = abs(len(self.nodes) - len(self.graph))
            for i in range(len(self.nodes)):
                if i < len(self.graph):
                    self.graph[i].extend([0] * extra)
                else:
                    self.graph.append([0] * len(self.nodes))

    def isValid(self, n1):
        return True if self.nodes.get(n1) != None else False

    def getdistance(self, n1, n2):
        if self.isValid(n1) and self.isValid(n2):
            return self.graph[self.nodes[n1]][self.nodes[n2]]
        print('Cannot get distance between non-existent nodes!')

    def setNodes(self, n1, n2, dist=1):
        if self.isValid(n1) and self.isValid(n2):
            self.graph[self.nodes[n1]][self.nodes[n2]] = dist
        else:
            print('Cannot set distance between non-existent nodes!')

    def printGraph(self):
        print(end='   ')  # 3 Spaces
        for i in self.nodes: (print(i, end='  '))  # 2 Spaces
        print()
        for i in range(len(self.graph)):
            print(list(self.nodes.keys())[i], self.graph[i])

    def getChildren(self, node):
        matrix = self.graph[self.nodes[node]]
        # print(matrix)
        answer = []
        # print(list(self.nodes.keys()))
        for i in range(len(matrix)):
            if matrix[i]: answer.append(list(self.nodes.keys())[i])
        return answer

    def unVisited(self, node, visited):
        for i in self.getChildren(node):
            if i not in visited:
                return i
        return None

    def dfs(self, visited: dict, stack: list):
        if not stack:
            return list(visited.keys())

        n = stack[-1]
        visited[n] = 1

        child = self.unVisited(n, visited)

        if child != None:
            stack.append(child)
            return self.dfs(visited, stack)
        else:
            return self.dfs(visited, stack[:-1:])

    def bfs(self, visited: dict, queue: list):
        if not queue:
            return list(visited.keys())

        v = queue.pop(0)
        visited[v] = 1

        for i in self.getChildren(v):
            if not visited.get(i) and i not in queue:
                queue.append(i)

        return self.bfs(visited, queue)


if __name__ == '__main__':
    g1 = Graph()
    g1.addNodes(0, 1, 2, 3, 4, 5, 6)

    for i in g1.getNodes():
        ele = map(int, input().split())
        for j in ele:
            g1.setNodes(i, j, 1)
    # print(g1.dfs({}, []))

    for i in g1.getNodes():
        print(g1.dfs({}, [i]))

'''
1 2
2
0 3
3 3

Sample Graph: 0-6 inclusive
Set for 0:1 3
Set for 1:0 2 5
Set for 2:1 3 4 5
Set for 3:0 2 4
Set for 4:2 3 6
Set for 5:1 2
Set for 6:1 4

1 3
0 2 5
1 3 4 5
0 2 4
2 3 6
1 2
1 4
'''
'''
B
A H
B D E
C
C H G F
E
E
E
'''
'''

B D
D E
A F
F G
G

F
'''