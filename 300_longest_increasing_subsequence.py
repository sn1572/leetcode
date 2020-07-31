# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:41:14 2019

@author: mbolding3
"""


class Solution:
    def lengthOfLIS(self, nums):
        '''
        n^2 solution
        '''
        LIS = len(nums)*[0]
        if len(LIS) == 0:
            return(0)
        LIS[-1] = 1
        for i in range(2, len(nums)+1):
            thisLIS = 1
            for j in range(-i+1, 0):
                if nums[j] > nums[-i]:
                    if LIS[j]+1 > thisLIS:
                        thisLIS = LIS[j]+1
            LIS[-i] = thisLIS
        return(max(LIS))


if __name__ == '__main__':
    test = [10,9,2,5,3,7,101,18]
    sol = Solution()
    print(sol.lengthOfLIS(test))