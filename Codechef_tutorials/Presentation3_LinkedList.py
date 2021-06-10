class Wagon:
    def __init__(self, wagon_value, wagon_number, next_node=None):
        self.value = wagon_value  # Wagon Property 1
        self.number = wagon_number  # Wagon Property 2
        self.next = next_node  # Pointer to next wagon(None by default)


class Train:
    def __init__(self, arg_head):
        self.head = Wagon(arg_head, 0)
        self.tail = None

    def addNodeAtHead(self, value, number):
        wagon = Wagon(value, number, next_node=self.head)
        self.head = wagon

    def addWagon(self, value, Number):
        x = self.head
        while x.next != None:  # First time x.next
            x = x.next
        #  next of x would be none
        x.next = Wagon(value, Number)

    #
    def traversal(self):
        x = self.head  # Stand near the engine or the first node(head)

        while x != None:
            print(x.value)
            x = x.next


t1 = Train("Driver")  # Initialized the train
# t1.head.next = Wagon("Passenger 1", 1)
# t1.head.next.next = Wagon("Passenger 2", 2)
# t1.head.next.next.next = Wagon("Passenger 3", 3)
# t1.head.next = Wagon("Passenger 1", 1)
# t1.head.next.next.next = Wagon("Passenger 3", 3)
# t1.head.next.next.next.next = Wagon("Passenger 3", 3)
