# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def toList(array):
    if array == []:
        return(None)
    else:
        head = ListNode(array[0])
        current = head
        for element in array[1:]:
            current.next = ListNode(element)
            current = current.next
        return(head)


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def getLength(node):
            '''
            O(n)
            '''
            L = 0
            while node is not None:
                L += 1
                node = node.next
            return(L)


        def reverseHalfInPlace(node, length):
            '''
            Reverses the first half of a linked list
            in place. O(n/2)
            Technically the tail of the new list 
            doesn't point to None, but it won't matter
            '''
            prev = node
            current = node.next
            for i in range(int(length/2)-1):
                temp, current.next = current.next, prev
                prev, current = current, temp
            if length % 2 == 0:
                return(prev, current)
            else:
                return(prev, current.next)


        L = getLength(head)
        if L == 0:
            return(True) #I guess?
        elif L == 1:
            return(True)
        elif L == 2:
            if head.val == head.next.val:
                return(True)
            else:
                return(False)
        elif L == 3:
            if head.val == head.next.next.val:
                return(True)
            else:
                return(False)
        else:
            left, right = reverseHalfInPlace(head, L)

        while right is not None:
            if left.val != right.val:
                return(False)
            left, right = left.next, right.next

        return(True)


if __name__ == '__main__':
    sol = Solution()
    test1 = toList([1,2,2,1])
    test2 = toList([1,2,5,7,5,2,1])
    test3 = toList([1,2,5,7,6,2,1])
    assert(sol.isPalindrome(test1) == True)
    assert(sol.isPalindrome(test2) == True)
    assert(sol.isPalindrome(test3) == False)