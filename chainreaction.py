# Project Description: The project had been made by me in the first year, back when I was learning the basic syntax
# of programming as well as OOP concepts.
#
# Why am I proud of it? I got the opportunity to apply OOP concepts that I had learned during the previous semester
# in this project such as chaining, giving meaningful properties to objects, methods, etc. I also implemented
# Depth-first-search unknowingly in my project. This project helped me grasp the concepts of OOP and use them at the
# same time. Thanks to this, I am no longer afraid of classes anymore!
#
# Working: This is a two-player CLI game that is made using python. The initial setup consists of a 10x10 grid. The
# two players take turns while playing and every time a choice is being made, the following things are checked:
#
# 1. Whether the square is already occupied by another player.
# 2. Whether the selection would cause a chain reaction.
# 3. Whether any of the players has won.
#
# The game ends when either of the players has occupied all existing selections.

class grid:
    def __init__(self, x, y, value, u, d, l, r):
        self.x = x
        self.y = y
        self.value = value
        self.up = u
        self.down = d
        self.left = l
        self.right = r


class Content:
    def __init__(self, capacity, filled, player):
        self.capacity = capacity
        self.filled = filled
        self.player = player


def play(z):
    while True:
        if z % 2 == 0:
            player = 'A'
        else:
            player = 'B'
        print('Player', player, 'will play!')
        print('Enter x and y coordinates of insertion:')
        try:
            d1 = int(input())
        except:
            print('Invalid Entry!')
            play(z)
            break
        try:
            d2 = int(input())
        except:
            print('Invalid Entry!')
            play(z)
            break
        m = search(d1, d2)
        c = checker(m, player)
        if c == 0:
            print('Entry cannot be made here!')
        else:
            insert(m, player)
            z += 1
        ###
        display()
        ###
        if z > 1:
            l = losecheck(glist)
            if l == 0:
                print('PLAYER B HAS WON!!')
                break
            elif l == 1:
                print('PLAYER A HAS WON!!')
                break


def search(x, y):
    for i in glist:
        if i.x == x and i.y == y:
            return i
    print("Error:Invalid input")
    return None


def insert(obj, player1):
    if obj.value.filled < obj.value.capacity:
        obj.value.player = player1
        obj.value.filled += 1

    elif obj.value.filled == obj.value.capacity:
        obj.value.filled = 0
        obj.value.player = 'N'

        l = [obj.up, obj.down, obj.left, obj.right]

        for i in l:
            if i:
                insert(i, player1)


def losecheck(glist):
    a = 0
    b = 0
    for i in glist:
        if i.value.player == 'A':
            a += 1
        elif i.value.player == 'B':
            b += 1
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return None


def display():
    for i in megagridlist:
        for j in i:
            m = search(j[0], j[1])
            print(str(m.value.filled) + str(m.value.player), end=' ')
        print()


def checker(obj, player1):
    if obj.value.player == player1 or obj.value.player == 'N':
        return 1
    else:
        return 0


###########################################################
if __name__ == '__main__':
    glist = []
    for i in range(0, 10):
        for j in range(0, 10):
            glist.append(grid(i, j, None, None, None, None, None))
    ### GLIST contains grid objects
    for i in glist:
        if i.x in (0, 9) and i.y in (0, 9):  # Corner cells
            i.value = Content(1, 0, 'N')
            if i.x == 0 and i.y == 0:
                i.right = search(0, 1)
                i.down = search(1, 0)
            elif i.x == 0 and i.y == 9:
                i.left = search(0, 8)
                i.down = search(1, 9)
            elif i.x == 9 and i.y == 0:
                i.up = search(8, 0)
                i.right = search(9, 1)
            elif i.x == 9 and i.y == 9:
                i.up = search(8, 9)
                i.left = search(9, 8)

        elif i.value == None and (i.x in (0, 9) or i.y in (0, 9)):  # Side rows
            i.value = Content(2, 0, 'N')
            if i.y == 0:
                i.right = search(i.x, 1)
                i.down = search((i.x + 1), (0))
                i.up = search((i.x - 1), (0))
            if i.x == 0:
                i.left = search((0), (i.y - 1))
                i.right = search((0), (i.y + 1))
                i.down = search((1), (i.y))
            if i.y == 9:
                i.up = search((i.x - 1), (9))
                i.down = search((i.x + 1), (9))
                i.left = search((i.x), (8))
            if i.x == 9:
                i.up = search((8), (i.y))
                i.left = search((9), (i.y - 1))
                i.right = search((9), (i.y + 1))
        else:  # Remaining grid
            i.value = Content(3, 0, 'N')
            i.up = search((i.x - 1), (i.y))
            i.down = search((i.x + 1), (i.y))
            i.left = search((i.x), (i.y - 1))
            i.right = search((i.x), (i.y + 1))
    ########################################################GRID
    megagridlist = []
    for i in range(0, 10):
        x = []
        for j in range(0, 10):
            x.append((i, j))
        # print(x)
        megagridlist.append(x)
    #####################################################

    player = ''
    z = 0
    display()

    play(z)
