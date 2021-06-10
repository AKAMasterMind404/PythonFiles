def calcTokenInLine(line):
    global numk
    print('line:', line)
    for index, i in enumerate(line):
        if i in numk.keys():
            numk[i] = numk[i] + 1
            line.pop(index)


def isToken(t):
    global keywords
    r1 = range(33, 44)
    r2 = range(123, 126)
    r3 = range(91, 95)
    r4 = range(58, 63)

    tokenOrds = list(r1) + list(r2) + list(r3) + list(r4)

    return t in keywords or ord(t) in tokenOrds


with open('cfile.txt', 'r') as f:
    keywords = {'float', 'double', 'main', }  # '(', ')', ';', '<', '>', '{', '}', '+', '-', '/', '*', '=']
    # keywords.extend([str(i) for i in range(10)])

    numk = {}
    for i in keywords:
        numk[i] = 0

    for i in f:
        line = i.strip()
        for j in line:
            if j == '#': break
            print(f'{j}:{isToken(j)}', end=' ')
        # print(line)
        print()
        # calcTokenInLine(line)
