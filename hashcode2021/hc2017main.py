import operator as o

class Endpoint:
    def __init__(self, id, latency, numCaches):
        self.id = id
        self.latency = latency
        self.numCaches = numCaches
        self.latencyToCache = {}


class Request:
    def __init__(self, videoID, endpointID, requests):
        self.videoID = videoID
        self.endpointID = endpointID
        self.requests = requests


if __name__ == '__main__':
    listOfEndPoints = []
    listOfRequests = []

    with open('h17ip.txt', 'r') as inputFile:
        V, E, R, C, X = map(int, inputFile.readline().strip().split())
        # print(V, E, R, C, X)
        videoSizes = list(map(int, inputFile.readline().strip().split()))

        for eID in range(E):
            datacenterLatency, caches = map(int, inputFile.readline().strip().split())
            # print(datacenterLatency, caches)
            e1 = Endpoint(eID, datacenterLatency, caches)

            for cL in range(caches):
                cacheServerNumber, cacheLatency = map(int, inputFile.readline().strip().split())
                # print(cacheServerNumber, cacheLatency)
                e1.latencyToCache[cacheServerNumber] = cacheLatency
            # print(e1.latencyToCache)
            listOfEndPoints.append(e1)

        for request in range(R):
            vid, eid, numr = inputFile.readline().strip().split()
            # print(vid)
            listOfRequests.append(Request(vid, eid, numr))
    #####
    endpointPrioritybyRequests=[]
    for ind,i in enumerate(listOfEndPoints):
        d=i.latencyToCache
        # for j in d.keys():
        endpointPrioritybyRequests.append([ind,sum(d.values())])

    print(endpointPrioritybyRequests)