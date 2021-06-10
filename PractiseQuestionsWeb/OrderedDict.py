from collections import OrderedDict

o1=OrderedDict()
items=int(input())
for i in range(items):
    theInput=input().split()
    price=int(theInput[-1])
    commodity=' '.join(theInput[0:len(theInput)-1])
    # print(commodity)
    # print(price)

    if commodity in o1:
        o1[commodity]+=price
    else:
        o1[commodity]=price

for i in o1:
    print(i,o1[i])