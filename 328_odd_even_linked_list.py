# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddCurrent = head
        try:
            evenHead = head.next
        except:
            return(head)
        evenCurrent = evenHead
        while oddCurrent is not None and evenCurrent is not None:
            oddPast = oddCurrent
            if oddCurrent.next is not None:
                oddCurrent = oddPast.next.next
            else:
                oddCurrent = None
            oddPast.next = oddCurrent
            evenPast = evenCurrent
            if evenCurrent.next is not None:
                evenCurrent = evenPast.next.next
            else:
                evenCurrent = None
            evenPast.next = evenCurrent
        if oddCurrent is None:
            oddPast.next = evenHead
        else:
            oddCurrent.next = evenHead
        return(head)