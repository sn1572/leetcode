# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:44:45 2019

@author: mbolding3
"""

class Solution:


    def crawl(self, grid, i, j):
        try:
            grid[i][j] = ['1',1]
            for x, y in [(max(i-1,0),j), (i+1,j), (i,max(j-1,0)), (i,j+1)]:
                try:
                    if int(grid[x][y][0]):
                        try:
                            grid[x][y][1]
                        except:
                            self.crawl(grid, x, y)
                except:
                    pass
        except:
            pass


    def numIslands(self, grid):
        count = 0
        if not grid:
            return(count)
        H, W = len(grid), len(grid[0])
        for i in range(H):
            for j in range(W):
                current = grid[i][j]
                if int(current[0]):
                    try:
                        current[1]
                    except:
                        count += 1
                        self.crawl(grid,i,j)
        return(count)


if __name__ == '__main__':

    sol = Solution()

    test1 = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]
    test1 = list(map(lambda x: list(map(lambda y: str(y), x)), test1))

    test2 = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
    test2 = list(map(lambda x: list(map(lambda y: str(y), x)), test2))

    test3 = [['0']]
    test4 = [['1','1'],
             ['0','1']]
    test5 = [["1","0","1","1","0","1","1"]]

    print(sol.numIslands(test1))
    print(sol.numIslands(test2))
    print(sol.numIslands(test3))
    print(sol.numIslands(test4))
    print(sol.numIslands(test5))