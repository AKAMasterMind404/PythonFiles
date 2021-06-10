def TOH(n, fromTower, toTower, helpTower):
    if n:
        TOH(n - 1, fromTower, helpTower, toTower)
        toTower.append(fromTower.pop())
        TOH(n - 1, helpTower, toTower, fromTower)


def display():
    l1 = len(r1)
    l2 = len(r2)
    l3 = len(r3)

    m = max(l1, l2, l3)
    ml = len(str(max(r1 + r2 + r3)))
    e1 = e2 = e3 = ' ' * ml

    for i in range(m, -1, -1):
        if i < l1:
            e1 = r1[i]
        if i < l2:
            e2 = r2[i]
        if i < l3:
            e3 = r3[i]
        print('{} {} {}'.format(e1, e2, e3))

    print('_ _ _')


if __name__ == '__main__':
    g = 0
    n = int(input())

    r1 = [i for i in range(n, 0, -1)]
    r2 = []
    r3 = []
    display()
    # print(r1)
    # print(r2)
    # print(r3)
    print('######')
    TOH(n, r1, r3, r2)
    # print(r1)
    # print(r2)
    # print(r3)

    display()
# //*[@id="disks"]/div[1]
