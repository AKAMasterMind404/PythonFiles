import sys
import time

sys.setrecursionlimit(9999999)
"""

    5
    4    3
    3,2

"""


def dp_Fibonacci(num):
    global hashtable

    if hashtable.get(num): return hashtable.get(num)

    ans = dp_Fibonacci(num - 1) + dp_Fibonacci(num - 2)
    hashtable[num] = ans

    return ans


def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


hashtable = {0: 0, 1: 1, 2: 1, 3: 2}

if __name__ == '__main__':
    t1 = time.time()
    fibonacci(999)
    print(time.time() - t1)

    t1 = time.time()
    dp_Fibonacci(999)
    print(time.time() - t1)
