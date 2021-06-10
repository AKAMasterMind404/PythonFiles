from itertools import combinations
from itertools import permutations
import operator


class Vehicle:
    def __init__(self, id, x, y, time):
        self.id = id
        self.x = x
        self.y = y
        self.time = time

    def check(self, tr: int) -> bool:
        return self.time <= tr


def getDistance(a, b, x, y):
    return abs(a - x) + abs(b - y)


def setDistance(vehicle: Vehicle, x1, y1):
    vehicle.x = x1
    vehicle.y = y1


def hypRide(rideinfo, v: Vehicle) -> tuple:
    global t
    # go to
    a, b = rideinfo[1]
    x, y = rideinfo[2]

    vx = v.x
    vy = v.y
    vt = v.time
    print('time:',vt)
    # go there
    distance = getDistance(vx, vy, a, b)  # vehicles init position and starting position of destination
    print(f'Distance to a,b is {vx}')
    if v.check(t) and vt + distance <= t:
        vx, vy = a, b
        vt = distance
        print(vt,distance)
        print(f'Vehicle travelled to {a,b}. Vt set to {vt}')
        # setDistance(v, a, b)
        # v.time = v.time + distance
    else:
        print('Not enough time')
        return False,False

    earliest_start = rideinfo[3]

    if earliest_start < t:
        print(f'Earliest start is {earliest_start} bypassed {t}.')
        return False,False
    elif earliest_start == t:
        print('bonus')
        print(f'Vehicle travels to {x,y}')
        return True, True
        # setDistance(v, x, y)
    else:
        print(f'Vehicle travels to {x,y}')
        return True, False
        # wait
        # v.time = earliest_start
        # setDistance(v, x, y)


def rideTo(rideinfo, v: Vehicle):
    global t
    # go to
    a, b = rideinfo[1]
    x, y = rideinfo[2]

    # go there
    distance = getDistance(v.x, v.y, a, b)  # vehicles init position and starting position of destination

    if v.check(t) and v.time + distance <= t:
        setDistance(v, a, b)
        v.time = v.time + distance
    else:
        return

    earliest_start = rideinfo[3]

    if earliest_start < v.time:
        return
    elif earliest_start == v.time:
        print('bonus')
        setDistance(v, x, y)
    else:
        # wait
        v.time = earliest_start
        setDistance(v, x, y)


with open('18ip.txt', 'r') as ip:
    r, c, numVehicles, numRides, bonus, t = map(int, ip.readline().strip().split())

    vehicleInfo = []

    for i in range(numVehicles):  # 3
        vehicleInfo.append(Vehicle(i, 0, 0, 0))

    rideInfo = []
    for ride in range(numRides):
        a, b, x, y, start, end = map(int, ip.readline().strip().split())
        rideInfo.append(
            [
                ride,  # 0 ride number
                (a, b),  # 1 start coordinates
                (x, y),  # 2 end coordinates
                start,  # 3 start ride by
                end,  # 4 end ride by
            ]
        )

    grid = [[0 for i in range(c)] for j in range(r)]
    # grid[0][0] = 1
    # print(grid)
    for i in sorted(rideInfo,key=operator.itemgetter(3)):
        for car in vehicleInfo:
            print(hypRide(i,car))
            print(i)
            print()