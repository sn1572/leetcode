class Solution(object):
    def countPrimes(self, n, *args):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 2:
            return(0)
        sieve = dict(zip(range(2,n), (n-2)*[0]))
        index = 2
        while index**2 <= n:
            try:
                sieve[index]
                for j in range(index, n//index+1):
                    try:
                        del sieve[index*j]
                    except:
                        pass
            except:
                pass                
            index += 1
        try:
            if args[0]:
                return(sieve)
        except:
            pass
        return(len(sieve.keys()))


if __name__ == '__main__':
    sol = Solution()
    assert(sol.countPrimes(4) == 2)
    assert(sol.countPrimes(5) == 2)
    assert(sol.countPrimes(6) == 3)
    assert(sol.countPrimes(10) == 4)
    assert(sol.countPrimes(11) == 4)
    assert(sol.countPrimes(12) == 5)
    assert(sol.countPrimes(10000) == 1229)