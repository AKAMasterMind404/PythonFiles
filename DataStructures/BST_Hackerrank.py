class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.parent = None


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.info, end=' '),
        inorderTraversal(root.right)


def notEntirelyNone(list1): return list1.count(None) < len(list1)


def preOrder(root):
    if root == None:
        return None
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            x = self.root
            node = Node(val)
            while True:
                if val > x.info and not x.right:  # x.right==None hence x.right = False not False ==True Insertion takes place
                    node.parent = x
                    x.right = node
                    break
                elif val > x.info and x.right:
                    x = x.right
                if val < x.info and not x.left:  # x.left==None hence x.left = False not False ==True Insertion takes place
                    node.parent = x
                    x.left = node
                    break
                elif val < x.info and x.left:
                    x = x.left

    def search(self, v):
        x = self.root
        while x:
            if v > x.info:
                x = x.right
            elif v < x.info:
                x = x.left
            elif v == x.info:
                return x

    def lowestCommonAncestor(self, n1, n2):
        n1 = self.search(n1)
        n2 = self.search(n2)

        # Consider n1 to be at higher level than n2
        cp1 = n1.parent

        while n2.parent != self.root:
            if n2.parent == cp1:
                return cp1
            else:
                n2 = n2.parent
        if cp1 == n2.parent:
            return cp1
        else:
            cp2 = n2.parent

            while n1.parent != self.root:
                if n1.parent == cp2:
                    return cp2
                else:
                    n1 = n1.parent
            if cp2 == n1.parent:
                return cp2

    def treeHeight(self, isPrint):
        x = [self.root]
        if isPrint and notEntirelyNone(x):
            print(x[0].info)
        minHeight = -1
        maxHeight = -1
        minCaptured = False  # Boolean counter that checks whether minimum height has been recorded

        listOfLevels = []

        while notEntirelyNone(x):  # CHECKS WHETHER ALL ELEMENTS IN X ARE NOT NONE
            maxHeight += 1
            if not minCaptured:
                minHeight += 1
            listOfLevels.append(x)

            temp = []
            for i in x:
                if i:
                    if i.left:
                        temp.append(i.left)
                        if isPrint:
                            print(i.left.info, end=' ')
                    else:
                        temp.append(None)
                        if isPrint:
                            print(None, end=' ')
                    if i.right:
                        temp.append(i.right)
                        if isPrint:
                            print(i.right.info, end=' ')
                    else:
                        temp.append(None)
                        if isPrint:
                            print(None, end=' ')
                else:
                    temp.append(None)
                    temp.append(None)
                    if isPrint:
                        print(None, end=' ')
                        print(None, end=' ')

            if isPrint:
                print()
            x = temp
            if None in temp:
                minCaptured = True

        if minHeight < 0: minHeight = 0
        if maxHeight < 0: maxHeight = 0

        print("Max:", maxHeight)
        print("Min:", minHeight)
        return listOfLevels


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(4)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(7)
    tree.insert(6)
    tree.treeHeight(True)  # ENTER TRUE FOR PRINTING THE TREE / FALSE FOR PRINTING MIN AND MAX HEIGHT OF TREE
