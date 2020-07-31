class Solution(object):


    def __init__(self):
        self.vals = {1: '1', 2: '11'}
        self.last = 2


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """


        def calcNext(m):
            #m is a str
            out = ''
            count = 0
            current = m[0]
            for char in m:
                if char == current:
                    count += 1
                else:
                    out = out+str(count)+current
                    count = 1
                    current = char
            out = out+str(count)+current
            return(out)


        try:
            return(self.vals[n])
        except:
            while self.last < n:
                self.last += 1
                self.vals[self.last] = calcNext(self.vals[self.last-1])
            return(self.vals[n])