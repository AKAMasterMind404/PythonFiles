# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        h2, length = head, 1
        while h2.next:
            h2 = h2.next
            length += 1

        h2 = head

        for z in range(k - 1): h2 = h2.next

        e1, h2 = h2, head

        for z in range(length - k): h2 = h2.next

        e2 = h2

        e1.val, e2.val = e2.val, e1.val

        return head
