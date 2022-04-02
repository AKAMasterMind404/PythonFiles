# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if not root: return []
        stack = [root]

        ans = []
        while stack:
            newstack = []
            maxele = stack[0].val
            for i in stack:
                if i.val > maxele:
                    maxele = i.val
                if i.left:
                    newstack.append(i.left)
                if i.right:
                    newstack.append(i.right)
            ans.append(maxele)
            stack = newstack
        return ans