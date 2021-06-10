def notEntirelyNone(list1):
    return list1.count(None) < len(list1)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


class Node:
    def __init__(self, value):
        self.info = value
        self.parent = None
        self.left = None
        self.right = None


class Heap:
    def __init__(self):
        self.root = None
        self.curlevel = []

    def search(self, root, val):
        if root.info == val:
            return root
        else:
            self.search(root.left, val)
            self.search(root.right, val)

    def insert(self, val, x):
        node = Node(val)
        if self.root == None:
            self.root = node
        else:
            isIn = False
            temp = []
            for i in x:
                if not i.left:
                    node.parent = i
                    i.left = node
                    isIn = True
                    break
                else:
                    temp.append(i.left)
                if not i.right:
                    node.parent = i
                    i.right = node
                    isIn = True
                    break
                else:
                    temp.append(i.right)
            if not isIn:
                self.insert(val, temp)

    def printHeap(self):
        x = [self.root]
        if notEntirelyNone(x):
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
                        print(i.left.info, end=' ')
                    else:
                        temp.append(None)
                        print(None, end=' ')
                    if i.right:
                        temp.append(i.right)
                        print(i.right.info, end=' ')
                    else:
                        temp.append(None)
                        print(None, end=' ')
                else:
                    temp.append(None)
                    temp.append(None)
                    print(None, end=' ')
                    print(None, end=' ')

            print()
            x = temp

    def sortedInsertion(self, val):
        self.insert(self.root, val)

        element = self.search(self.root, val)


if __name__ == '__main__':
    h1 = Heap()
    h1.insert(10, [h1.root])
    h1.insert(12, [h1.root])
    h1.insert(14, [h1.root])
    h1.insert(16, [h1.root])
    h1.insert(18, [h1.root])

    h1.printHeap()
