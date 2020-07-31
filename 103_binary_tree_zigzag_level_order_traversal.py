class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def combine(self, right, left, order):
        R = len(right); L = len(left)
        shortest = (right if R <= L else left)
        longest = (right if R >= L else left)
        S = len(shortest)
        for i in range(S):
            if order:
                shortest[i] = left[i]+right[i]
            else:
                shortest[i] = right[i]+left[i]
            order = not order
        if longest[S:]: # fires iff longest[S:] is not an empty list
            shortest += longest[S:]
        return(shortest)


    def zigzagLevelOrder(self, root, order = True):
        # order is true if using English standard reading orienration,
        # aka left to right. By default, the root node is sorted "in order."

        if root is None:
            return([])
        elif root.right == None and root.left == None:
            return([[root.val]])
        else:
            zig = self.zigzagLevelOrder(root.right, not order)
            zag = self.zigzagLevelOrder(root.left, not order)
            return([[root.val]] + self.combine(zig, zag, not order))


if __name__ == '__main__':
    test = TreeNode(3)
    test.left = TreeNode(9)
    test.right = TreeNode(20)
    test.right.right = TreeNode(7)
    test.right.left = TreeNode(15)
    test.right.right.right = TreeNode(100)
    sol = Solution()
    print(sol.zigzagLevelOrder(test))