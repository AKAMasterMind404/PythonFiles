# Date: 10/02/2021
# Author: Atharv Manish Karbhari


class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertNode(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
            self.length += 1
        else:
            x = self.head
            while x.next:
                x = x.next
            n.prev = x
            x.next = n
            self.tail = n
            self.length += 1

    def printList(self):
        x = self.head
        while x:
            print(x.value, end='->')
            x = x.next
        print(None)

    def findNode(self, val):
        x = self.head
        while x:
            if x.value == val:
                return x
            else:
                x = x.next

    def deleteNode(self, val):
        isDel = False
        if self.head.value == val:
            self.head.next.prev = None
            self.head = self.head.next
            isDel = True
        elif self.tail.value == val:
            newTail = self.tail.prev
            self.tail.prev = None
            newTail.next = None
            self.tail = newTail
            isDel = True
        else:
            if self.findNode(val):
                x = self.head
                while x.value != val:
                    x = x.next
                x.next.prev = x.prev
                x.prev.next = x.next
                x.next = None
                x.prev = None
                isDel = True
        if isDel:
            self.length -= 1

    def insertAtHead(self, val):
        n = Node(val)
        n.next = self.head
        self.head.prev = n
        self.head = n
        self.length += 1

    def insertAtIndex(self, val, index):
        if index >= self.length: return
        if not index:
            self.insertAtHead(val)
        elif index == self.length - 1:
            self.insertNode(val)
        else:
            z = 1
            x = self.head
            while z < index:
                x = x.next
                z += 1
            n = Node(val)
            n.next = x.next
            n.prev = x
            x.next = n
            x.next.next.prev = n
            self.length += 1

    def exchangeNodes(self, n1, n2):
        v1 = self.findNode(n1)
        v2 = self.findNode(n2)

        if v1 and v2:
            v1.value = n2
            v2.value = n1

    def nodeAtIndex(self, i):
        e = self.head
        z = 0
        if i < self.length:
            while z < i:
                e = e.next
                z += 1
            return e

    def exchangeNodesWithIndex(self, i1, i2):
        n1 = self.nodeAtIndex(i1)
        n2 = self.nodeAtIndex(i2)
        n1.value, n2.value = n2.value, n1.value


if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.insertNode(10)
    l1.insertNode(20)
    l1.insertNode(30)
    l1.insertNode(40)
    l1.insertNode(50)
    l1.insertAtHead(0)
    # l1.insertAtIndex(60, 5)
    # l1.exchangeNodesWithIndex(0,6)

    print('head:', l1.head.value)
    print('tail:', l1.tail.value)
    print()

    l1.printList()
