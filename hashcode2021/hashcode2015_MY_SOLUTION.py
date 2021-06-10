class Server:
    def __init__(self, reqslots, cap):
        self.reqSlots = reqslots
        self.capacity = cap


def assignSlotsToServers(listOfservers): pass


def main():
    R, S, U, P, M = map(int, input().split())

    listOfUnavailableSlots = []

    for unavailableslot in range(U):
        listOfUnavailableSlots.append(tuple(map(int, input().split())))

    servers = []  # Contain server class objects

    for i in range(M):
        s, c = map(int, input().split())
        servers.append(Server(s, c))

    grid = [[0] * R] * S
    assignSlotsToServers(servers)


if __name__ == '__main__':
    main()
