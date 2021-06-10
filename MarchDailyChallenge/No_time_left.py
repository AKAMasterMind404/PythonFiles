n, timeNeeded, timeLeft = map(int, input().split())
timeZones = list(map(int, input().split()))[::-1]

r = 'NO'

for i in timeZones:
    if i + timeLeft >= timeNeeded:
        r = 'YES'
        break

print(r)
