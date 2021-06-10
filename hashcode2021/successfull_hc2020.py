import operator

f = open('b_read_on.txt', 'r')
b, l, d = map(int, f.readline().split(" "))
# print(b,l,d)
s = f.readline().strip().split(" ")
# print(s)
bts = {}
for i in range(b):
    bts.update({i: [i, int(s[i])]})
# print(bts)
t = []
n = []
for i in range(l):
    n1, t1, m1 = map(int, f.readline().split(" "))
    # t.update({i:[n1,t1,m1]})
    t.append([n1, t1, m1])
    n1 = list(map(int, f.readline().split(" ")))
    n.append(n1)
print(t)
print(n)
app = []
da = d
sco = []
for i in sorted(t, key=operator.itemgetter(1)):
    c = i[1]
    print(t.index(i))
    while da != 0 and c >= -1:
        c -= 1
        if (c < 0):
            p = []
            for k in n[t.index(i)]:
                if (k in app):
                    continue
                else:
                    p.append(bts[k])
            for j in sorted(p, key=operator.itemgetter(1), reverse=True)[:da * i[2]]:
                print(j)
                app.append(j[0])
                sco.append(j[1])
        da -= 1
v = 0
for i in sco:
    v = v + i
print("Score:", v)