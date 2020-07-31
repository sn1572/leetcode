from math import factorial as fct


class Solution(object):


    def ncr(self, n, r):
        return(fct(n)//(fct(n-r)*fct(r)))


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return(self.ncr(m+n-2, n-1))


if __name__ == '__main__':
    sol = Solution()