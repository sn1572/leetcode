class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return(0)
        result = 1
        while result**2 < x:
            result += 1
        if result**2 > x:
            result -= 1
        return(result)
        