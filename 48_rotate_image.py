class Solution(object):
    def rotate(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(M)
        for i in range(int(N/2)):
            for j in range(i,N-i-1):
                M[j][N-i-1], M[N-i-1][N-j-1], M[N-j-1][i], M[i][j] = M[i][j], M[j][N-i-1], M[N-i-1][N-j-1], M[N-j-1][i]


if __name__ == '__main__':
    sol = Solution()
    test1 = np.arange(4).reshape((2,2))
    test2 = np.arange(9).reshape((3,3))
    test3 = np.arange(16).reshape((4,4))