from itertools import combinations as c
from itertools import permutations as p
from collections import Counter
import operator as o
from collections import namedtuple
import math


def goodNess(string: str) -> tuple:
    S, N = string, len(string)
    goodness = 0
    notGood = 0

    for i in range(N // 2):
        if S[i] != S[(i + 1) * -1]:
            goodness += 1
        else:
            notGood += 1

    return goodness, notGood


for case in range(int(input())):
    # Process
    ans = None  # initialization

    N, K = map(int, input().split())

    S = input()
    extraGoodness = 0
    g = goodNess(S)

    currGN = g[0]

    ans = K - g[0]

    print(f'Case #{case + 1}:', ans)
