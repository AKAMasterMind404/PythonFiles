class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertNodeAtEnd(self, val):
        if not self.head:
            n = Node(val)
            self.head = n
            self.tail = n
            self.head.next = self.head
            self.length += 1
        else:
            n = Node(val)
            x = self.head
            while x.next != self.head:
                x = x.next

            self.tail = n
            n.next = self.head
            x.next = n
            self.length += 1

    def printCircularList(self, *i):
        z = 0
        x = l1.head
        while x:
            print(x.value, end='->')
            x = x.next

            if len(i) and z >= self.length - 1:
                break
            else:
                z += 1
        print(None)

    def insertNodeAtStart(self, val):
        if self.head:
            n = Node(val)
            n.next = self.head
            self.tail.next = n
            self.head = n
            self.length += 1
        else:
            self.insertNodeAtEnd(val)

    def deleteNode(self, index):  # Pending
        if self.head == self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            if not index:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.length -= 1
            elif index == self.length - 1:
                before = self.head
                z = 1

                while z < index:
                    before = before.next
                    z += 1

                self.tail = before
                self.length -= 1
            else:
                before = self.head
                z = 1

                while z < index:
                    before = before.next
                    z += 1

                before.next = before.next.next
                self.length -= 1

    def insertNodeAtIndex(self, val, index):
        if not index:
            self.insertNodeAtStart(val)
        elif index >= self.length:
            self.insertNodeAtEnd(val)
        else:
            n = Node(val)
            z = 1
            x = self.head
            while z < index:
                x = x.next
                z += 1
            n.next = x.next
            x.next = n
            self.length += 1


l1 = CircularLinkedList()

l1.insertNodeAtEnd(10)
l1.insertNodeAtEnd(20)
l1.insertNodeAtStart(5)
# l1.insertNodeAtStart(5)
# l1.insertNodeAtIndex(12,0)
# l1.deleteNode(0)

# 5 10 20
# l1.insertNodeAtIndex(1.5, 2)
print()
l1.printCircularList(1)
