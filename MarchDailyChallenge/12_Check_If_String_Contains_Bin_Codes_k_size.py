
def subRefiner(string, k):
    new = '0' * (k - len(string)) + string
    return new


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        z = 0
        mnum = [subRefiner(bin(i)[2::],k) for i in range(2 ** k)]
        l1 = dict()
        while z < len(s):
            subs = s[z:z + k]
            l1[subs]=1
            z += 1
        # print(l1)
        for i in mnum:
            if not l1.get(i):
                return False
        return True


s1 = Solution()
print(s1.hasAllCodes(s = "0110", k = 1))
