class UndergroundSystem:

    def __init__(self):
        self.booking = dict()  # {}
        self.averageBetween = dict()

    def checkIn(self, id, inPlace, time):
        global ansList
        self.booking[id] = [inPlace, time]
        ansList.append(None)

        # print(self.booking)

    def checkOut(self, id, outPlace, outTime):
        global ansList
        if id in self.booking.keys():
            v = self.booking[id]
            # print("Checked in:", k, v)
            # print("To check out:", id, outPlace, outTime)
            # print()
            theKey = tuple(sorted([v[0], outPlace]))
            if theKey not in self.averageBetween.keys():
                self.averageBetween[theKey] = [outTime - v[1]]
            else:
                self.averageBetween[theKey].append(outTime - v[1])
        ansList.append(None)

    def getAverageTime(self, cinplace, coutplace, ):
        global ansList
        l = self.averageBetween[tuple(sorted([cinplace, coutplace]))]
        ans = sum(l) / len(l)
        ansList.append(ans)
        return ans


ansList = []

undergroundSystem = UndergroundSystem()  #
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
undergroundSystem.getAverageTime("Leyton", "Paradise")  # // return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
undergroundSystem.getAverageTime("Leyton", "Paradise")  # // return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
undergroundSystem.getAverageTime("Leyton", "Paradise")

print(ansList)
