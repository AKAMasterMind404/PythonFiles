# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    fa, fo = 0, 0
    al = len(apples)
    ol = len(oranges)
    r = al if al > ol else ol

    # theRange=[i for i in range(s,t+1)]
    # if len(theRange)==0:
    #     theRange=[i for i in range(s,t+1,-1)]

    for i in range(r):
        if i < al:
            if a + int(apples[i]) in range(s, t + 1):
                fa += 1
        if i < ol:
            if b + int(oranges[i]) in range(s, t + 1):
                fo += 1
    print(fa)
    print(fo)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
