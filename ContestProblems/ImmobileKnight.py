for _ in range(int(input())):
    n, m = map(int, input().split())
    rows = [0 for i in range(n)]
    cols = [0 for i in range(n)]
    pairs = []

    for i in range(m):
        x, y = map(int, input().split())
        rows[x - 1] += 1
        cols[y - 1] += 1
        pairs.append((x, y))

    print(pairs)
    ans = "YES"
    for x,y in pairs:
        rows[x - 1] -= 1
        cols[y - 1] -= 1

        print(rows)
        print(cols)

        if rows.count(0) == 0 and cols.count(0) == 0:
            ans = "NO"
            break

        rows[x - 1] += 1
        cols[y - 1] += 1
    print(ans)
