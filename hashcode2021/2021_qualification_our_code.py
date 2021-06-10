from itertools import combinations as c
from itertools import permutations as p
import operator
from collections import namedtuple
import math

from DataStructures import Graph_Adjacency_matrix as g

g1 = g.Graph()
g1.addNodes([0, 1, 2, 3, 4])
g1.setNodes(2, 0, 1)
g1.setNodes(2, 1, 3)
g1.setNodes(2, 3, 2)
g1.setNodes(3, 1, 1)
g1.setNodes(0, 1, 1)


def getIntersectionConnections():
    i = {}
    for node in g1.nodes:
        connected = []
        for index, j in enumerate(g1.getChildren(node)):
            if j:
                connected.append(index)
        i[node] = connected
    return i


def increaseCarPointer(car):
    global carInfo
    carInfo[car][3] += 1

def getCarsWaitingAtIntersection():
    pass
    # for i in
print(getIntersectionConnections())
with open('ip2021.txt', 'r') as ip:
    duration, intersections, numStreets, numcars, bonus = map(int, ip.readline().strip().split())
    # print(duration, intersections, numStreets, numcars, bonus)
    streetInfo = []

    connections = {}

    for sID in range(numStreets):
        tIP = ip.readline().strip().split()
        # print(tIP)
        iStart, iEnd = int(tIP[0]), int(tIP[1])
        streetName = tIP[2]
        streetLength = int(tIP[3])

        streetInfo.append([
            sID,  # 0 street id
            [iStart, iEnd],  # 1 intersection at start and end
            streetName,  # 2 name of the street
            streetLength,  # 3 # Time taken for a car to cross the length of a street
            iEnd,  # 4
        ])

    carInfo = []

    for car in range(numcars):
        tIP = ip.readline().strip().split()
        # print(tIP)
        streetsToTravel = int(tIP[0])
        streets = tIP[1::]
        carInfo.append([
            car,  # 0 car number
            streetsToTravel,  # 1
            streets,  # 2
            0,  # 3
        ]
        )

    for i in streetInfo: print(i)
    print()
    increaseCarPointer(0)
    for i in carInfo: print(i)
