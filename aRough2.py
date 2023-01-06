t = input()
r = 'aeiou'
b = ''

for i in t:
    if i.lower() in r:
        b += '0'
    else:
        b += '1'

print(int(b, 2))
print("abcDef".title())