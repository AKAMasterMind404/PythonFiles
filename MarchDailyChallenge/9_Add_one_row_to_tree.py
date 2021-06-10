# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth < 2:
            return TreeNode(val, root)
        else:
            x = [root]
            while depth > 2:
                t = []

                for i in x:
                    if i.left:
                        t.append(i.left)
                    if i.right:
                        t.append(i.right)

                x = t
                depth -= 1

            for i in x:
                leftSubtree = i.left
                rightSubtree = i.right
                i.left = TreeNode(val,leftSubtree)
                i.right = TreeNode(val,None,rightSubtree)

            return root