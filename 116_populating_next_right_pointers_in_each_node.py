# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:48:49 2020

@author: mbolding3
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:


    def connect_trees( self, left, right ):
        # Connecting two trees which are already themselves
        # connected is easy. Just connect the right side of the
        # left tree to the left side of the right tree.
        if left is None:
            return()
        left.next = right
        self.connect_trees( left.right, right.left )


    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return( root )
        self.connect( root.left )
        self.connect( root.right )
        self.connect_trees( root.left, root.right )
        return( root )