# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return(False)
        index = 0
        seent = {id(head): index}
        while head.next is not None:
            index += 1
            head = head.next
            memAdress = id(head)
            try:
                seent[memAdress]
                return(True)
            except:
                seent[memAdress] = index
        return(False)