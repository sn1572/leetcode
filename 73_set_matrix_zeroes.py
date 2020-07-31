# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:10:25 2020

@author: mbolding3
"""


import sys


class Solution(object):


    flag = 1.1


    def setFlags(self, i, j):

        def block(x,y):
            val = matrix[x][y]
            if val:
                matrix[x][y] = flag

        matrix, m, n, flag = self.matrix, self.m, self.n, Solution.flag
        for r in range(0,i):
            block(r,j)
        for r in range(i+1,m):
            block(r,j)
        for c in range(0,j):
            block(i,c)
        for c in range(j+1,n):
            block(i,c)


    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        flag = Solution.flag
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.m, self.n = m, n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.setFlags(i,j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == flag:
                    matrix[i][j] = 0


if __name__ == '__main__':
    print('size of an int in Python:', sys.getsizeof(1), 'bytes.')
    print('size of a float in Python:', sys.getsizeof(1.1), 'bytes.')

    M = [[0,0,0,5],
         [4,3,1,4],
         [0,1,1,4],
         [1,2,1,3],
         [0,0,1,1]]

    S = Solution()
    S.setZeroes(M)