# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        l = [root]
        z = 0

        if depth > 1:
            for i in range(1, depth - 1):
                temp = []

                for i in l:
                    if i: temp.extend([i.left, i.right])

                l = temp

            l = [i for i in l if i]
            for i in l:
                obLeftchild = i.left
                obRightchild = i.right
                i.left = TreeNode(val, obLeftchild, None)
                i.right = TreeNode(val, None, obRightchild)

        else:
            return TreeNode(val, root, None)

        return root
