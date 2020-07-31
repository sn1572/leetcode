# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:06:16 2019

@author: mbolding3
"""


from bisect import bisect_left as bl


class Solution:


    def diagSearch(self, matrix, target):
        limit = min(len(matrix), len(matrix[0]))
        left, right = 0, limit-1
        while left != right:
            m = (left+right)//2
            val = matrix[m][m]
            if val == target:
                return(m)
            if val < target:
                left = m if m>left else m+1
            else:
                right = m if m<right else m-1
        return(right)


    def searchMatrix(self, matrix, target):
        """
        Idea: Perform a "binary" chop on the matrix by
        examining the diagonals. The first four "if"s handle
        corner cases (empty matrices, matrices with one row or
        column, matrices whose entries are all too large or too small).

        Now we perform a binary search along the diagonal of the matrix, and
        discover an index i such that matrix[i][i] is the largest diagonal
        element x such that x >= target.

        We may then discard the submatrices matrix[:i, :i] and matrix[i:, i:]
        from consideration, since we know from the special problem constraints
        that every entry in the first submatrix is too small, and every
        entry in the second submatrix is too large.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return(False)
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return(False)
        if len(matrix) == 1:
            matrix = matrix[0]
            index = bl(matrix, target)
            if matrix[index] == target:
                return(True)
            return(False)
        if len(matrix[0]) == 1:
            col = list(map(lambda x: x[0], matrix))
            index = bl(col, target)
            if col[index] == target:
                return(True)
            return(False)

        diagIndex = self.diagSearch(matrix, target)
        val = matrix[diagIndex][diagIndex]
        if val == target:
            return(True)
        else:
            newMat = matrix[:diagIndex]
            newMat = list(map(lambda x: x[diagIndex:], newMat))
            bool1 = self.searchMatrix(newMat, target)
            newMat = matrix[diagIndex:]
            if val < target:
                newMat = list(map(lambda x: x[:diagIndex+1], newMat))
            else:
                newMat = list(map(lambda x: x[:diagIndex], newMat))
            bool2 = self.searchMatrix(newMat, target)
            return(bool1 or bool2)


if __name__ == '__main__':
    sol = Solution()
    test = [[1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
    test2 = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]]