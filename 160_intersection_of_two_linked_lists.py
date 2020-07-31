# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def toLinkedList(list):
    head = None
    prev = None
    current = None
    for element in list:
        current = ListNode(element)
        try:
            prev.next = current
            prev = current
        except:
            prev = ListNode(element)
            head = prev
    return(head)


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """


        def length(node):
            '''
            Gets the length of a linked list
            '''
            L = 0
            while node is not None:
                L += 1
                node = node.next
            return(L)


        LA = length(headA)
        LB = length(headB)

        currentA = headA
        currentB = headB

        if LB > LA:
            currentA, currentB = currentB, currentA

        diff = abs(LA-LB)
        while diff > 0:
            currentA = currentA.next
            diff -= 1

        while currentA is not None:
            if currentA == currentB:
                return(currentA)
            else:
                currentA = currentA.next
                currentB = currentB.next

        return(None)


if __name__ == '__main__':
    test1 = toLinkedList([5,0,1])
    test2 = toLinkedList([4,1,8,4,5])
    test1.next.next.next = test2.next.next
    sol = Solution()
    result = sol.getIntersectionNode(test1,test2)