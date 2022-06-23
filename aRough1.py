l1 = ['a']
l2 = ['a']
l3 = ['c']
l4 = ['d']
l5 = ['e']

dic1 = {"l1": l1, "l2": l2, "l3": l3, "l4": l4, "l5": l1}

[print(i) for i in dic1.keys() if not dic1.get(i)]
