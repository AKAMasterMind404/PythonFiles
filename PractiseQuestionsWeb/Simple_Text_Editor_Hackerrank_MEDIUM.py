s, cache = "", []


def append(s, operand):
    global cache
    cache.append(s)
    return s + operand


def delete(s, operand):
    global cache
    cache.append(s)
    return s[:-int(operand):]


for _ in range(int(input())):
    theInput = input().split()
    qtype = theInput[0]
    operand = None
    if len(theInput) == 2:
        operand = theInput[1]
    if qtype == '1':
        s = append(s, operand)
    elif qtype == '2':
        s = delete(s, operand)
    elif qtype == '3':
        print(s[int(operand) - 1])
    elif qtype == '4':
        s = cache.pop(-1)