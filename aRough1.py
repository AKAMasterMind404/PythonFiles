n = int(input())

sp = "  "
for i in range(n - 1):
    print((sp * i) + str(i + 1) + sp * (n - i - 1) * 2 + str(i + 1) + (sp * i))

print(sp*(n-1) + " " + str(n))

for i in range(n - 2, -1, -1):
    print((sp * i) + str(i + 1) + sp * (n - i - 1) * 2 + str(i + 1) + (sp * i))
