import operator as o

text = "my name is khan and i am not a terrorist"

appeared = dict()

for i in text:
    if appeared.get(i):
        appeared[i] += 1
    else:
        appeared[i] = 1

newL = sorted(list(appeared.items()), key=o.itemgetter(1))
[print(i) for i in newL]

# 8 skills aur 25 Quests
