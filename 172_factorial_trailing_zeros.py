class Solution(object):


    def __init__(self):
        self.powers = {0:1}
        exponent = 1
        while exponent < 14:
            self.powers[exponent] = 5**exponent
            exponent += 1


    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        power = 0
        for key, val in self.powers.items():
            if n < val:
                break
            power = key
        #power is now the highest power less than n
        fives = 0
        for i in range(1,power+1):
            fives += n // self.powers[i]
        return(fives)


if __name__ == '__main__':
    sol = Solution()
    assert(sol.trailingZeroes(0) == 0)
    assert(sol.trailingZeroes(4) == 0)
    assert(sol.trailingZeroes(5) == 1)
    assert(sol.trailingZeroes(25) == 6)
    assert(sol.trailingZeroes(30) == 7)
    assert(sol.trailingZeroes(31) == 7)