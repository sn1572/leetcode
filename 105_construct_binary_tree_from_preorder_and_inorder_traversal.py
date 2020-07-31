# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 08:38:23 2019

@author: mbolding3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return(None)
        elif len(preorder) == 1:
            return(TreeNode(preorder[0]))

        in_Rt = inorder.index(preorder[0]) # in_Rt = inorder's root

        preLeft = preorder[1:in_Rt+1]
        preRight = preorder[in_Rt+1:]
        inLeft = inorder[:in_Rt]
        inRight = inorder[in_Rt+1:]

        thisRoot = TreeNode(preorder[0])
        thisRoot.left = self.buildTree(preLeft, inLeft)
        thisRoot.right = self.buildTree(preRight, inRight)
        return(thisRoot)


if __name__ == '__main__':
    testPre = [3,9,20,15,7]
    testIn = [9,3,15,20,7]

    sol = Solution()
    tree = sol.buildTree(testPre, testIn)

    testPre = [1,2,3]
    testIn = [1,2,3]

    tree = sol.buildTree(testPre, testIn)

    testPre = [3,2,1,4]
    testIn = [1,2,3,4]

    tree = sol.buildTree(testPre, testIn)