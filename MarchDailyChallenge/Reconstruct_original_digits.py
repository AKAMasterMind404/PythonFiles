DIGITS = [
    [0,'z',[]],
    [2,'w',[]],
    [4,'u',[]],
    [6,'x',[]],
    [8,'g',[]],
    [5,'f',[4]],
    [7,'s',[6]],
    [3,'h',[8]],
    [9,'i',[6,8,5]],
    [1,'o',[0,2,4]]
]
class Solution:
    def originalDigits(self, S: str) -> str:
        fmap, ans, n = [0] * 26, [0] * 10, len(S)
        for i in range(10):
            dig, char, rems = DIGITS[i]
            count = S.count(char)
            for rem in rems: count -= ans[rem]
            ans[dig] += count
        return "".join([str(i) * ans[i] for i in range(10)])