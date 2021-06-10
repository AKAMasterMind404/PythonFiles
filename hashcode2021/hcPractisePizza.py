import operator
from itertools import combinations as c
from itertools import permutations as p


def mergeAndFind(combo):
    if len(combo) == 2:
        newlist = []
        [newlist.extend([i, j]) for i in combo[0] for j in combo[1]]
        # print(len(set(newlist)),2)
        r = len(list(set(newlist)))  # / 2
        return r
    elif len(combo) == 3:
        newlist = []
        [newlist.extend([i, j, k]) for i in combo[0] for j in combo[1] for k in combo[2]]
        # print(len(set(newlist)), 3)
        r = len(list(set(newlist)))  # / 3
        return r
    elif len(combo) == 4:
        newlist = []
        [newlist.extend([i, j, k, l]) for i in combo[0] for j in combo[1] for k in combo[2] for l in combo[3]]
        # print(len(set(newlist)),4)
        r = len(list(set(newlist)))  # / 4
        return r


def pizzaNumber(combos):
    global pizzas
    pizzaNumbers = []
    for i in combos:
        for j in pizzas:
            if j.ingredients == i:
                pizzaNumbers.append(j.index)
    return pizzaNumbers


def getPizzas(tup):
    return [j for i, j in enumerate(pizzaIngredients) if i in tup]


class Pizza:
    def __init__(self, index, num, ingredients, ):
        self.index = index  # Int
        self.numberOfIngredients = num  # Int
        self.ingredients = ingredients  # List


def removePizza(*pizzaNumbers):
    global pizzas
    newPizas = []
    for i in range(len(pizzas)):
        if i not in pizzaNumbers:
            newPizas.append(pizzas[i])
    return newPizas


# class Combo:

if __name__ == '__main__':
    with open('hcPI.txt', 'r') as f:

        M, T2, T3, T4 = map(int, f.readline().strip().split())
        pizzas = []

        uniqueIngredients = []
        pizzaIngredients = []

        removedPizzas = []

        for i in range(M):
            ip = f.readline().strip().split()
            pizzas.append(Pizza(i, int(ip[0]), ip[1::]))
            uniqueIngredients.extend(ip[1::])
            pizzaIngredients.append(ip[1::])

        print(pizzas)

        uniqueIngredients = list(set(uniqueIngredients))
        print('These are the number of ingredients:', len(uniqueIngredients))
        # for i in pizzaIngredients:print(i)
        combos = []
        for i in range(2, 5):
            [combos.append(getPizzas(j)) for j in c(range(M), i)]

        maxratio, resindex = mergeAndFind(combos[0]), 0

        ratioAndCombos = []
        distinctRatios = []

        twoCombos = []
        threeCombos = []
        fourCombos = []

        for i, cmb in enumerate(combos):
            ratio = mergeAndFind(cmb)
            ratioAndCombos.append([ratio, cmb])
            distinctRatios.append(ratio)
            # print(ratio,i)
            # print(maxratio,resindex)
            # print()
            if ratio > maxratio:
                maxratio = ratio
                resindex = i
                # print(f'maxratio:{maxratio},resindex={resindex}')

        print(maxratio, resindex)

        Best_Combo = combos[resindex]
        MostEffNumber = len(Best_Combo)
        PizzaNumbers = pizzaNumber(combos[resindex])

        sortedRatiosAndCombos = sorted(ratioAndCombos, key=operator.itemgetter(0))

        for i in ratioAndCombos:
            print(i)
        print('\n\n\n\n')
        for i in sortedRatiosAndCombos:
            print(i)
        distinctRatios = sorted(list(set(distinctRatios)), reverse=True)
        print(distinctRatios)
        # sevenWaleCombos=[]

        # for i in  distinctRatios:

        # for i in distinctRatios:
        # with open('output.txt','a+'):
