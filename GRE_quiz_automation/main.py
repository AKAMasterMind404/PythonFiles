import os
import random as r


def takeOutARandomWord():
    maxIndex = len(l) - 1
    randomIndex = r.randint(0, maxIndex)
    word = l.pop(randomIndex)
    return word


if __name__ == '__main__':
    l = list()

    with open(f'{os.path.abspath("")}/bank3.txt') as f:
        for i in f:
            l.append(i.strip())

        while l:
            print(takeOutARandomWord())
            input()
