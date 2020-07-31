# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return([])
        trav = self.inorderTraversal(root.left)
        trav.append(root.val)
        trav += self.inorderTraversal(root.right)
        return(trav)


if __name__ == '__main__':
    test = TreeNode(1)
    test.right = TreeNode(2)
    test.right.left = TreeNode(3)
    sol = Solution()
    print(sol.inorderTraversal(test))