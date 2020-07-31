# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        
        def iterReverse(node):
            if node == None:
                return None
            current = node
            newHead = ListNode(node.val)
            while current.next is not None:
                newNode = ListNode(current.next.val)
                newNode.next = newHead
                newHead = newNode
                current = current.next
            return(newHead)

        
        def recurReverse(node):
            if node == None:
                return(None, None)
            else:
                if node.next is not None:
                    previous, newHead = recurReverse(node.next)
                    current = ListNode(node.val)
                    previous.next = current
                    return(current, newHead)
                else:
                    newHead = ListNode(node.val)
                    return(newHead, newHead)

            
        #newHead = iterReverse(head)
        #return(newHead)

        unused, newHead = recurReverse(head)
        return(newHead)