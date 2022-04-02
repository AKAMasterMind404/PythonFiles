class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = None
        second = None
        prev = TreeNode(float('-inf'))

        def inorder(root):
            nonlocal first, second, prev

            if not root:
                return

            inorder(root.left)
            if not first and root.val <= prev.val:
                first = prev

            if first and root.val <= prev.val:
                second = root

            prev = root
            inorder(root.right)

        inorder(root)
        temp = first.val
        first.val = second.val
        second.val = temp

