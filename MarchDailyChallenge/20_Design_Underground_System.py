from collections import Counter


class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        self.freqs = Counter()

    def checkIn(self, id, stationName, t):
        self.ids[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        Name2, t2 = self.ids.pop(id)
        self.pairs[(Name2, stationName)] += t - t2
        self.freqs[(Name2, stationName)] += 1

    def getAverageTime(self, startStation, endStation):
        return self.pairs[startStation, endStation] / self.freqs[startStation, endStation]
