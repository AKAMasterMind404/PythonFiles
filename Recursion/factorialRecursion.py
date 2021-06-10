import time
from functools import lru_cache


@lru_cache(9999)
def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacciDP(num):
    global h
    if num == 1 or num == 0:
        return num
    else:
        if h.get(num):
            return h.get(num)
        else:
            ans = fibonacci(num - 1) + fibonacci(num - 2)
            h[num] = ans
            return ans
