# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        
        def findDepth(node):
            if node == None:
                return 0
            elif node.right == node.left == None:
                return 1
            else:
                return(max(1+findDepth(node.left), 1+findDepth(node.right)))
        
        return(findDepth(root))