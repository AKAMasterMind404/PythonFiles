class Element:
    def __init__(self, prev, value, next):
        self.prev = prev
        self.value = value
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, element):
        if self.head == None:
            self.head = Element(None, element, None)
            self.tail = Element(None, element, None)
        else:
            e = Element(self.tail, element, None)
            self.tail.next = e
            self.tail = e

    def deleteNode(self, value):
        try:
            if value == self.head.value == self.tail.value:
                self.head = self.tail = None
            elif value == self.tail.value:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            elif value == self.head.value:
                x = self.tail
                while x.prev.prev != None:
                    x = x.prev
                x.prev.next = None
                x.prev = None
                self.head = x
            else:
                x = self.tail
                while x != None:
                    if x.value == value:
                        x.prev.next = x.next
                        x.next.prev = x.prev
                        break
                    x = x.prev
        except AttributeError:
            pass

    def returnValuesList(self):
        emp = []
        x = self.tail
        while x != None:
            emp.append(x.value)
            x = x.prev
        return emp[::-1]

    def returnList(self):
        emp = []
        x = self.tail
        while x != None:
            emp.append(x)
            x = x.prev
        return emp[::-1]
