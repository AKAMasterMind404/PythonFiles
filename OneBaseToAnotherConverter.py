# SEMESTER - 2, B.Tech CSE

def valuegiver(coode):
    length = len(str(coode))
    values = []
    z = 0
    while z <= length - 1:
        dig = coode[z]
        for i in dic:
            if str(dic.get(i)) == dig:
                values.append(i)
        z += 1
    return values


def DecimalConverter(code, base):
    base = int(base)
    values = valuegiver(code)  # list
    l = len(values) - 1
    z = 0
    cc = 0
    while l >= 0:
        cc += (values[z]) * (base ** l)
        z += 1
        l -= 1
    return cc


def Code1toanother(code, base1, base2):
    base1 = int(base1)
    base2 = int(base2)
    dcode = DecimalConverter(code, base1)
    code = ''
    while dcode > 0:
        # print(dcode,base2,dcode%base2,dic.get(dcode%base2))
        code += str(dic.get(dcode % base2))
        dcode = int(dcode / base2)
    x = ''
    z = len(code) - 1
    while z >= 0:
        x += code[z]
        z -= 1
    code = x
    return code


dic = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
       16: 'G', 17: 'I', 18: 'J', 19: 'K', 20: 'L',
       21: 'M', 22: 'N', 23: 'O', 24: 'P', 25: 'Q', 26: 'R', 27: 'S', 28: 'T', 29: 'U', 30: 'V', 31: 'W', 32: 'X',
       33: 'Y', 34: 'Z'}

if __name__ == '__main__':
    code = input('Enter code here:')
    base = input('Specify the base:')
    convert = input('Convert to base:')

    print(Code1toanother(code, base, convert))
