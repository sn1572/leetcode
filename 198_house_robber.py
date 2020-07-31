class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        L = len(nums)
        if L == 0:
            return(0)
        elif L == 1:
            return(nums[0])

        prevs = {}
        current = 2
        
        prevs[0] = nums[0]
        prevs[1] = max(nums[0], nums[1])
        
        while current < L:
            newVal = nums[current] + prevs[current-2]
            oldVal = prevs[current-1]
            if newVal > oldVal:
                prevs[current] = newVal
            else:
                prevs[current] = oldVal
            current += 1

        return(prevs[L-1])


    '''
    #from the web:
    def rob(self, nums: 'List[int]') -> 'int':
        dp = 0, 0
        for num in nums:
            dp = dp[1] + num, max(dp)
        return max(dp)
    '''


if __name__ == '__main__':
    test1 = [2,7,9,3,1]
    test2 = [1,2,3,1]
    sol = Solution()
    assert(sol.rob(test1) == 12)
    assert(sol.rob(test2) == 4)