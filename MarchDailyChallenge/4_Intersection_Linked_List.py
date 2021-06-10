# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0

        currA = headA
        while currA:
            lenA = lenA + 1
            currA = currA.next

        currB = headB
        while currB:
            lenB = lenB + 1
            currB = currB.next

        currA = headA
        currB = headB

        if lenA > lenB:
            while lenA != lenB:
                lenA = lenA - 1
                currA = currA.next
        else:
            while lenA != lenB:
                lenB = lenB - 1
                currB = currB.next

        while lenA > 0:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
            lenA = lenA - 1

        return
