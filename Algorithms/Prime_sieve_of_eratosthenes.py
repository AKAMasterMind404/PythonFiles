def primeNumberinRange(num):
    d = {0: False, 1: False}

    for i in range(2, num + 1):
        d[i] = True
    # print(d)
    # Initialization of Dictionary

    initlimit = int(num ** 0.5) + 1  # Tag multiples of numbers up to this number as False

    for i in range(2, initlimit):
        # print(i,'::')
        if d[i]:
            starting = i ** 2  # IF D[I] IS ALREADY PRIME, ALL ITS MULTIPLES UNTIL D[I*I] ARE NON PRIME
        else:
            starting = 2 * i
        for j in range(starting, num + 1, i):
            if d[j]:
                d[j] = False
    #         print(j,end=' ')
    #     print()
    #
    # print(d)
    prList = []
    for i in d:
        if d[i]:
            prList.append(i)
            # print(i)
    return prList


def primeIn(ll, ul):
    upperLimit = ul
    lowerLimit = ll

    l = []
    for i in primeNumberinRange(upperLimit):
        if i >= lowerLimit:
            l.append(i)
    return l


def isPrime(num): return num in primeNumberinRange(num + 1)


# Return True if num is in List of Primes in range num + 1

print(primeNumberinRange(966289))
