# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':

        if l1 is None:
            return(l2)
        elif l2 is None:
            return(l1)

        current1 = l1
        current2 = l2

        if current1.val > current2.val:
                current1, current2 = current2, current1

        head = current1

        while current2 is not None:
            while current1.next is not None and current1.next.val < current2.val:
                current1 = current1.next
            if current1.next is None:
                current1.next = current2
                return(head)
            hold1 = current1.next
            hold2 = current2.next
            current1.next = current2
            current2.next = hold1
            current2 = hold2

        return(head)


def listToNodes(array):
    current = ListNode(array[0])
    head = current
    for i in range(1,len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return(head)


if __name__ == '__main__':
    test1 = listToNodes([1,2,4])
    test2 = listToNodes([1,3,4])
    sol = Solution()
    res = sol.mergeTwoLists(test1, test2)