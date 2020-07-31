'''
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
'''


class Solution(object):


    def __init__(self, board = None):
        self.board = board
        self.M = 0
        self.N = 0


    def rowSums(self):
        for i in range(self.M):
            for j in range(1,self.N):
                self.board[i][j] = self.board[i][j-1]+self.board[i][j]


    def squareVal(self, x, y):
        #i,j is upper left corner
        #k,l is lower right corner
        i = max(0, x-1)
        j = max(0, y-1)
        k = min(self.M-1, x+1)
        l = min(self.N-1, y+1)
        out = 0
        for iota in range(i,k+1):
            out += self.board[iota][l]-(self.board[iota][j-1] if j > 0 else 0)
        out -= self.board[x][y]-(self.board[x][y-1] if y > 0 else 0)
        return(out.real if type(out) == complex else out)


    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
        self.rowSums()
        for x in range(self.M):
            for y in range(self.N):
                check = self.squareVal(x,y)
                if check < 2 or check > 3:
                    board[x][y] += 1j
                elif check == 2:
                    val = self.board[x][y]-(self.board[x][y-1] if y > 0 else 0)
                    val = val.real if type(val) == complex else val
                    if val == 0:
                        board[x][y] += 1j
        for i in range(self.M):
            for j in range(self.N):
                self.board[i][j] = 1 if self.board[i][j].imag == 0 else 0


if __name__ == '__main__':
    test = [[0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]]
    sol = Solution(test)
    sol.gameOfLife(test)
    print(test)

'''
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''