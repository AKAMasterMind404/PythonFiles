# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.elements = []

    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.elements.append(node.val)
            self.dfs(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.dfs(root)
        return self.elements[k - 1]