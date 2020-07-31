# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):


    def combine(self, levels1, levels2):
        l1 = len(levels1)
        l2 = len(levels2)
        if l2 == 0:
            return(levels1)
        elif l1 == 0:
            return(levels2)
        out = list(map(lambda x: x[0]+x[1], zip(levels1,levels2)))
        if l1 >= l2:
            out += levels1[l2:]
        else:
            out += levels2[l1:]
        return(out)


    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return([])
        else:
            levels1 = self.levelOrder(root.left)
            levels2 = self.levelOrder(root.right)
            return([[root.val]]+self.combine(levels1, levels2))


if __name__ == '__main__':
    test = TreeNode(3)
    test.left = TreeNode(9)
    test.right = TreeNode(20)
    test.right.left = TreeNode(15)
    test.right.right = TreeNode(7)
    sol = Solution()
    print(sol.levelOrder(test))