class Solution(object):


    def buildOpen(self, strList):
        return(list(map(lambda string: '('+string, strList)))


    def buildClose(self, strList):
        return(list(map(lambda string: ')'+string, strList)))


    def generate(self, n, totOpen=0, totClose=0):
        out = []
        if totOpen < n:
            out += self.buildOpen(self.generate(n-1, totOpen+1, totClose))
        if totOpen > 0 and totClose < totOpen:
            out += self.buildClose(self.generate(n, totOpen, totClose+1))

        if out:
            return(out)
        else:
            return([''])


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return(self.generate(2*n))


if __name__ == '__main__':
    sol = Solution()