from collections import Counter


class Solution:
    def originalDigits(self, s):
        cnt = Counter(s)
        Digits = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        Corresp = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        Counters = [Counter(digit) for digit in Digits]
        Found = [0] * 10
        for it, C in enumerate(Counters):
            k = min(cnt[x] // C[x] for x in C)
            for i in C.keys(): C[i] *= k
            cnt -= C
            Found[Corresp[it]] = k

        return "".join([str(i) * Found[i] for i in range(10)])
