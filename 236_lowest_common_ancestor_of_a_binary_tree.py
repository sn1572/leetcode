# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:02:04 2020

@author: mbolding3
"""


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:


    def __init__( self ):
        self.root = None


    def reverse( self, node, last=None ):
        if node is None:
            return()
        self.reverse( node.left, node )
        self.reverse( node.right, node )
        node.right = last


    def get_ancestry( self, node ):
        # Assumes a reversed tree
        ancestry = []
        while node is not None:
            ancestry.append( node )
            node = node.right
        return( ancestry )


    def get_lca( self, p, q ):
        a_p = self.get_ancestry( p )
        a_q = self.get_ancestry( q )
        offset = -1
        limit = -min( len(a_p), len(a_q) )
        while ( offset-1 >= limit ) and ( a_p[ offset-1 ] == a_q[ offset-1 ] ):
            offset -= 1
        return( a_p[ offset ] )


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.root != root:
            self.reverse( root )
            self.root = root
        return( self.get_lca( p, q ) )


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    b.right = d
    sol = Solution()
    lca = sol.lowestCommonAncestor( a, d, c )
    print( lca.val )