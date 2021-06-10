from itertools import combinations as cmb
from itertools import permutations as prm
from collections import Counter as cnt
import operator as op
from collections import namedtuple
import math

for case in range(int(input())):
    # Process
    ans = None  # initialization

    matrix = []
    R, C = map(int, input().split())
    for row in range(R):
        matrix.append(list(map(int, input().split())))

    for r in range(R-1):
        r1,r2 = matrix[r],matrix[r+1]
        m = r


    print(f'Case #{case + 1}:', ans)