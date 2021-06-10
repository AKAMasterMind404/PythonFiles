# Date: 28/01/2021


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.vals = []

    def interChange(self, pos1, pos2):
        node1 = self.getNodeFromPosition(pos1)
        node2 = self.getNodeFromPosition(pos2)

        v1 = node1.value
        v2 = node2.value

        node1.value = v2
        node2.value = v1

    def insertListAt(self, l, position):
        [self.insertAt(i, position) for i in l]

    def extendList(self, *l):
        [self.addNode(i) for i in l]

    def setValue(self, val, pos):
        c = 0
        x = self.head
        while c < pos:
            c += 1
            x = x.next
        x.value = val

    def addNode(self, value):
        n = Node(value)
        if not self.head:
            self.head = n
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = n
        self.vals.append(value)

    def insertAtTheBegining(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n
        self.vals.append(value)

    def printList(self):
        x = self.head
        while x:
            print(x.value, end=' -> ')
            x = x.next
        print(None)

    def getLength(self):
        return len(self.vals)

    def getNodeFromValue(self, val):
        x = self.head
        while x:
            if x.value == val: return x
            x = x.next

    def deleteNodeAt(self, position):
        x = self.head
        c = 1

        if position >= self.getLength():
            return
        elif position < 0:
            position = abs(self.getLength() + position)
        elif position == 0:
            self.head = self.head.next
        elif position == self.getLength() - 1:
            while c < position:
                x = x.next
                c += 1
            x.next = None
        else:
            while c < position:
                x = x.next
                c += 1
            x.next = x.next.next
        self.vals.pop(position)

    def getNodeFromPosition(self, position):
        if position > self.getLength(): return
        c = 0
        x = self.head
        while c != position:
            x = x.next
            c += 1
        return x

    def insertAt(self, value, position):
        if position >= self.getLength():
            self.addNode(value)
            return
        elif position == 0:
            self.insertAtTheBegining(value)
            return
        n = Node(value)

        c = 1
        x = self.head

        while c != position:
            x = x.next
            c += 1

        nextNode = x.next
        n.next = nextNode
        x.next = n


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


if __name__ == '__main__':
    l1 = SinglyLinkedList()
    l1.addNode(1)
    l1.addNode(2)
    l1.addNode(3)
    l1.addNode(4)
    l1.addNode(5)
    l1.extendList(6, 7, 8, 9)
    l1.insertListAt(['hi', 'hello'], 5)
    l1.printList()
