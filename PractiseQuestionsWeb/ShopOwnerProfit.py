from collections import Counter as c

totalSizes = int(input())

shoesSizes = dict(c(list(map(int, input().split()))))

# print(shoesSizes)
customers = int(input())

earning = 0

for i in range(customers):
    demand = list(map(int, input().split()))
    size = demand[0]
    price = demand[1]

    if size in shoesSizes:
        if shoesSizes[size]>0:
            earning+=price
            shoesSizes[size]-=1

print(earning)