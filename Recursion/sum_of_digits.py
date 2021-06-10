def sumDigits(d,s):
    inners=0
    if len(d)==1:
        inners+=int(d[0])
    else:
        inners+=int(d[0]) + sumDigits(d[1::],s)
    return inners

print(sumDigits('345',0))