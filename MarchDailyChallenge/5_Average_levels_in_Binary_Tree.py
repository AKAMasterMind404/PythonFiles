# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        x = [root]
        levels = []
        ans = []

        while x:
            t = []
            nL = []
            for i in x:
                if i:
                    t.extend([i.left, i.right])
                    nL.append(i.val)

            levels.append(nL)
            if nL:
                ans.append(sum(nL) / len(nL))
            x = t

        return ans
