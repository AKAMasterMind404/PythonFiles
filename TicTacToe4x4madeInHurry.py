# MADE BY VEDANT LANDGE B.TECH(CSE)


import random as r

r0 = ["-", "-", "-", "-", ]
r1 = ["-", "-", "-", "-", ]
r2 = ["-", "-", "-", "-", ]
r3 = ["-", "-", "-", "-", ]

keys = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [0, 3],
    5: [1, 0],
    6: [1, 1],
    7: [1, 2],
    8: [1, 3],
    9: [2, 0],
    10: [2, 1],
    11: [2, 2],
    12: [2, 3],
    13: [3, 0],
    14: [3, 1],
    15: [3, 2],
    16: [3, 3],
}


def printGrid():
    print(r0)
    print(r1)
    print(r2)
    print(r3)


def isOccupied(x, y):
    if x == 0:
        return r0[y] != "-"
    if x == 1:
        return r1[y] != "-"
    if x == 2:
        return r2[y] != "-"
    if x == 3:
        return r3[y] != "-"


def updateGrid(x, y, isCross: bool):
    res = ""
    if isCross:
        res = "X"
    else:
        res = "O"

    if x == 0:
        r0[y] = res
    elif x == 1:
        r1[y] = res
    elif x == 2:
        r2[y] = res
    elif x == 3:
        r3[y] = res


def isFilled():
    return (
            r0.count("-") == 0 and
            r1.count("-") == 0 and
            r2.count("-") == 0 and
            r3.count("-") == 0)


def checkWin(name):
    rowsAllFilledWithX = r0.count("X") == 4 or r1.count("X") == 4 or r2.count("X") == 4 or r3.count("X") == 4
    rowsAllFilledWithO = r0.count("0") == 4 or r1.count("0") == 4 or r2.count("0") == 4 or r3.count("0") == 4

    columnFilledWithX = ((r0[0] == "X" and r1[0] == "X" and r2[0] == "X" and r3[0] == "X") or
                         (r0[1] == "X" and r1[1] == "X" and r2[1] == "X" and r3[1] == "X") or
                         (r0[2] == "X" and r1[2] == "X" and r2[2] == "X" and r3[2] == "X") or
                         (r0[3] == "X" and r1[3] == "X" and r2[3] == "X" and r3[3] == "X"))

    columnFilledWithO = ((r0[0] == "O" and r1[0] == "O" and r2[0] == "O" and r3[0] == "O") or
                         (r0[1] == "O" and r1[1] == "O" and r2[1] == "O" and r3[1] == "O") or
                         (r0[2] == "O" and r1[2] == "O" and r2[2] == "O" and r3[2] == "O") or
                         (r0[3] == "O" and r1[3] == "O" and r2[3] == "O" and r3[3] == "O"))

    diagonalsFilledWithX = (r0[0] == "X" and r1[1] == "X" and r2[2] == "X" and r3[3] == "X") or \
                           (r0[3] == "X" and r1[2] == "X" and r2[1] == "X" and r3[0] == "X")

    diagonalsFilledWithO = (r0[0] == "O" and r1[1] == "O" and r2[2] == "O" and r3[3] == "O") or \
                           (r0[3] == "O" and r1[2] == "O" and r2[1] == "O" and r3[0] == "O")

    if rowsAllFilledWithX or columnFilledWithX or diagonalsFilledWithX:
        print(f"{name} wins")
        return True
    if rowsAllFilledWithO or columnFilledWithO or diagonalsFilledWithO:
        print("O wins")
        return True
    return False


if __name__ == '__main__':
    num = 0
    name = input("Enter your name: ")
    while True:
        x, y = None, None
        symbol = "X"

        if num % 2 == 0:
            x, y = keys[int(input().strip())]
        if num % 2 == 1:
            x, y = r.randrange(0, 4), r.randrange(0, 4)
            print()
            symbol = "O"

        if isOccupied(x, y):
            print("Already occupied!")
        else:
            num += 1
            updateGrid(int(x), int(y), symbol == "X")
            printGrid()

        if checkWin(name):
            break
        if isFilled():
            print("DRAW")
            break

