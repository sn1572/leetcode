class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        '''
        num = bin(n)
        counts = 0
        for i in range(len(num)):
            if num[i] == '1':
                counts += 1
        return(counts)
        '''
        
        
        counts = 0
        while n != 0:
            if n&1:
                counts += 1
            n = n>>1
        return(counts)