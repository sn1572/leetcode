# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':


        def makeBabies(array):
            if len(array) == 0:
                return(None)
            L = len(array)
            m = int(L/2)
            N = TreeNode(array[m])
            N.left = makeBabies(array[:m])
            N.right = makeBabies(array[m+1:])
            return(N)


        head = makeBabies(nums)
        return(head)