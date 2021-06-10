from itertools import combinations_with_replacement as c

def getDistinctIngredients(combo):
    l=[]
    for i in cmb:
        l.extend(i[2])
    return list(set(l))

with open('pizza2_ip/pizza_2ip.txt', 'r') as ip:
    p, oneTeam, twoTeam, threeTeam = map(int, ip.readline().strip().split())

    pizzas = []

    for i in range(p):
        _input = ip.readline().strip().split()
        pizza = [
            i,  # 0 pizza number
            int(_input[0]),  # 1 number of ingredients
            _input[1::],  # 2 list of ingredients
        ]
        pizzas.append(pizza)

    # for i in pizzas:
    #     print(i)

    for clength in range(2,5):
        for cmb in c(pizzas, clength):
            for i in cmb:
                print(cmb, '###', getDistinctIngredients(i),)