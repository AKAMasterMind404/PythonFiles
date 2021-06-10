#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    faster = v1
    slower = v2

    if v2 > v1:
        faster, slower = slower, faster
        x1, x2 = x2, x1

    # x1 for faster, x2 for slower
    while x2 > x1:
        x1 += faster
        x2 += slower
        # print(x1)
        # print(x2)
        if x1 == x2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
