# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, node):
        if not node:
            return None
        current = node.next
        prev = node
        prev.next = None
        while current:
            tmp = current.next
            current.next = prev
            current = tmp
            prev = current
        return(prev)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        