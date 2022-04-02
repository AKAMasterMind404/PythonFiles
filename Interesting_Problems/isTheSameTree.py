# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        _p = p is None
        _q = q is None
        if _p and _q:
            return True
        elif not _p and not _q:
            return p.val == q.val \
                   and self.isSameTree(p.left, q.left) \
                   and self.isSameTree(p.right, q.right)
        else:
            return False
