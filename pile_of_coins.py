def findBin(num):
    return int(bin(num)[2::])


def canRemove(x, pileSize):
    return x & pileSize == 0


t = int(input())
players = ['Anjali', 'Vaibhavi']

for case in range(t):
    pileSize = int(input())
    pile = ['stone'] * pileSize
    if pileSize == 1:
        print(players[1])
    else:
        z = 0
        r = len(pile)
        while len(pile):
            player = players[z]
            if canRemove(r, len(pile)):
                pile = pile[r::]
                print(pile)
                if z == 0:
                    z = 1
                    # z=1
                else:
                    z = 0
            else:
                if z == 0:
                    print(players[0])
                    break
                    # z=1
                else:
                    print(players[1])
                    break
