# 1()
def a():
    radius = int(input())

    PI = 3.1415926535

    area = PI * (radius ** 2)
    circumference = 2 * PI * radius

    print('Area is', area)
    print('Circumference is', circumference)


def b():
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())

    l1 = [s1, s2, s3]

    l = len(set(l1))

    if l == 1:
        print('Equilateral Triangle.')
    elif l == 2:
        print('Isosceles Triangle.')
    elif l == 3:
        print('Scalene Triangle.')


def c():
    s = 0
    for i in range(1, 11):
        s += i
    print('Sum of first 10 natural numbers is:', s)


def d():
    n = int(input())

    for i in range(1, 11):
        print(n, '*', i, '=', n * i)


def e():
    bikePrice = int(input())

    taxPercent = None

    if bikePrice in range(50001):
        taxPercent = 5
    elif bikePrice in range(50001, 100001):
        taxPercent = 10
    elif bikePrice > 100000:
        taxPercent = 20
    print('Tax percent is', taxPercent)
    tax = bikePrice * taxPercent / 100
    cp = bikePrice + tax
    print("Cost of thee bike including tax is", cp, " and the tax amount is", tax)


def f():
    fruits = ['Orange', 'Apple', 'Mango', 'Grapes', 'Raspberry', 'Banana']

    # f i)
    print(fruits)

    # f ii)
    print(len(fruits))

    # f iii)
    print(fruits[0])

    # f iv)
    print(fruits[4])


def g():
    # g i)
    integer = type(5)
    print(integer)

    # g ii)
    decimal = type(54.56)
    print(decimal)

    # g iii)
    text = type('hello')
    print(text)

    # g iv)
    boolean = type(True)
    print(boolean)


g()
