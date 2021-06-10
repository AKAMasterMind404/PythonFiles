def dirReduc(arr):
    stack = []
    opp = {("NORTH", "SOUTH"): 1, ("EAST", "WEST"): 1, ("SOUTH", "NORTH"): 1, ("WEST", "EAST"): 1}

    while arr:
        stack.append(arr.pop(0))

        if opp.get(tuple(stack[-2::])):
            stack.pop(-1)
            stack.pop(-1)
    return stack


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# a = ["SOUTH"]

print(dirReduc(a))
