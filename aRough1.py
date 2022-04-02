# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, n1: TreeNode, n2: TreeNode):
        if n1 and n2:
            n1.val += n2.val
            n1.left = self.dfs(n1.left, n2.left)
            n1.right = self.dfs(n1.right, n2.right)
            return n1
        else:
            return n1 or n2

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.dfs(root1, root2)
