import operator
from itertools import combinations as c


def getVerticalCombinations(verticalImages):
    return [list(i) for i in c(verticalImages, 2)]
    # for i in c(verticalImages,2):print(i)


def makeHorizontalSet(verticalCombo):
    picture = [
        pic,  # 0 id of the picture
        orientation,  # 1 the orientation of the picture
        numTags,  # 2 number of tags in this picture
        tags  # 3 list containing the tags of a picture
    ]
    newTags = list(set(verticalCombo[0][3] + verticalCombo[1][3]))
    print([[verticalCombo[0][0], verticalCombo[1][0]], 'H', len(newTags), newTags])
    return [[verticalCombo[0][0], verticalCombo[1][0]], 'H', len(newTags), newTags]


def calculateScore(s1, s2):
    s1 = set(s1[3])
    s2 = set(s2[3])

    return min(len(s1.intersection(s2)), len(s1 - s2), len(s2 - s1))


with open('19ips/a_example.txt', 'r') as ip:
    photos = int(ip.readline().strip())

    photoData = []

    vertical = []

    horizontal = []

    for pic in range(photos):
        data = ip.readline().strip().split()
        orientation = data[0]
        numTags = int(data[1])
        tags = data[2::]

        picture = [
            pic,  # 0 id of the picture
            orientation,  # 1 the orientation of the picture
            numTags,  # 2 number of tags in this picture
            tags  # 3 list containing the tags of a picture
        ]

        if orientation == 'H':
            horizontal.append(picture)
        else:
            vertical.append(picture)
        photoData.append(picture)

    allImages = horizontal

    verticalImages = getVerticalCombinations(vertical)

    for i in verticalImages:
        allImages.append(makeHorizontalSet(i))

    finalSlideCombos = []

    # for i in range(len(allImages) + 1):
    score = 0
    for j in c(allImages, len(allImages)):
        # print(j)

        z = 0

        try:
            while z < len(j):
                score += calculateScore(j[z], j[z + 1])
                z += 1
        except IndexError:
            pass

        # print(f'Score for {j} is {score}.\n')
        finalSlideCombos.append([j, score, score * len(j) / 100])

    winner = sorted(finalSlideCombos, key=operator.itemgetter(2))[-1]
    print(f'Score is:{score}.')
    # print('Score is:',s)
    # Output file
    winner = winner[0]
    with open('19op.txt', 'w+') as op:
        l = len(winner)
        op.write(f'{l}\n')
        for i in winner:
            if type(i[0]) != list:
                i[0] = [i[0]]
            for j in i[0]:
                op.write(f'{j} ')
            op.write('\n')
