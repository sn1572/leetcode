import math

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = len(nums)
        if L <= 1:
            return([nums])
        out = math.factorial(L)*[0]
        multiplicity = math.factorial(L-1)
        for i in range(L):
            num = nums[i]
            arrays = self.permute(nums[:i]+nums[i+1:])
            for j in range(multiplicity):
                out[i*multiplicity+j] = [num] + arrays[j]
        return(out)


if __name__ == '__main__':
    sol = Solution()