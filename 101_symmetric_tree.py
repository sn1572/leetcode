# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':


        def compare(node1, node2):
            if node1 == node2 == None:
                return(True)
            elif node1 is None or node2 is None:
                return(False)

            if node1.left is not None:
                if node2.right is None:
                    return(False)
                elif node2.right.val != node1.left.val:
                    return(False)
            elif node1.left is None:
                if node2.right is not None:
                    return(False)

            if node1.right is not None:
                if node2.left is None:
                    return(False)
                elif node2.left.val != node1.right.val:
                    return(False)
            elif node1.right is None:
                if node2.left is not None:
                    return(False)

            return(compare(node1.left, node2.right) and compare(node1.right, node2.left))


        if root is None:
            return(True)
        elif not compare(root, root):
            return(False)
        else:
            return(compare(root.left, root.right))