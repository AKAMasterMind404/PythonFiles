import random as r


def encrypt(i, n):
    def rep(output):
        dict = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
                'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q',
                'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a',
                'y': 'b', 'z': 'c', ' ': ' ',
                '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8', '7': '9', '8': '0', '9': '1', '0': '2',
                '.': '.', ',': ',', '/': '/',
                '(': '(', ')': ')', ':': ':'}
        back = ''
        for i in output.lower():
            for j in dict:
                if dict.get(j) == i:
                    back += j
        return back

    for j in range(0, n):
        i = rep(i)
    return i


for num in range(6):
    i = input('Enter text here:')
    j = r.randint(1, 27)
    print('Encrypted Text:', encrypt(i, j))
    print('Decryption code:', j)
