# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import bisect


class Solution(object):

    
    def __init__(self):
        self.calls = 0


    def kthSmallest(self, root, k, *args):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        try:
            smol = args[0]
            if root is None:
                return(None)
            val = root.val
            bisect.insort_left(smol, val)
            if self.calls >= k:
                smol.pop()
            self.calls += 1
            self.kthSmallest(root.left, k, smol)
            self.kthSmallest(root.right, k, smol)
        except:
            smol = [root.val]
            self.calls = 1
            self.kthSmallest(root.left, k, smol)
            self.kthSmallest(root.right, k, smol)
            self.calls = 0
            return(smol[-1])


if __name__ == '__main__':
    sol = Solution()

    test1 = TreeNode(3)
    test1.right = TreeNode(4)
    test1.left = TreeNode(1)
    test1.left.right = TreeNode(2)

    test2 = TreeNode(5)
    test2.right = TreeNode(6)
    test2.left = TreeNode(3)
    test2.left.right = TreeNode(4)
    test2.left.left = TreeNode(2)
    test2.left.left.left = TreeNode(1)