def test(n):
    if n < 4:
        return(n)
    elif n == 4:
        return(1)
    val = int(n**0.5)**2
    if val == n:
        return(1)
    leastSquares = n//val
    remainder = n-leastSquares*val
    while remainder > 0:
        val = int(remainder**0.5)**2
        quotient = remainder//val
        leastSquares += quotient
        remainder -= quotient*val
    return(leastSquares)

'''
class Solution:


    def __init__(self):
        self.memo = {0:0, 1:1, 2:2, 3:3, 4:1}


    def numSquares(self, n: int) -> int:
        if n in self.memo:
            return(self.memo[n])
        val = int(n**0.5)**2
        if val == n:
            return(1)
        leastSquares = n//val
        remainder = n-leastSquares*val
        while remainder > 0:
            val = int(remainder**0.5)**2
            quotient = remainder//val
            leastSquares += quotient
            remainder -= quotient*val
        lowerBound = int((n/(leastSquares-1))**0.5)
        for x in range(lowerBound, int(n**0.5)):
            test = test = n//(x**2) + self.numSquares(n%(x**2))
            if test < leastSquares:
                leastSquares = test
        self.memo[n] = leastSquares
        return(leastSquares)
'''

class Solution:
    #web solution

    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            print(toCheck)
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(4))
    print(sol.numSquares(25))
    #print(sol.numSquares(4703))
    #for i in range(65):
        #print(str(i)+'__'+str(sol.numSquares(i)))
    #for i in range(13,200):
     #   if test(i) != sol.numSquares(i):
      #      print(i)