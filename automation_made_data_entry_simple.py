length = 0

with open('ab.txt', 'r') as f:
    for line in f:
        length += 1

with open('ab.txt', 'r') as f:
    x = 0
    ans = ""
    for i in f:
        if i != '\n':
            ans += i.strip()[2::].strip()
            if x != length - 1:
                ans += " || "
        x += 1
    print(ans)

"A b i 4 t P"