#import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''
        if n <= 0:
            return(False)
        if str(math.log(n,3)).split('.')[-1] == '0':
            return(True)
        return(False)
        '''

        return 3486784401%n == 0 if n > 0 else False