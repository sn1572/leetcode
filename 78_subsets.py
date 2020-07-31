class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]
        if nums == []:
            return([[]])
        for i in range(len(nums)):
            num = nums[i]
            for subset in self.subsets(nums[i+1:]):
                out.append([num]+subset)
        return(out)


if __name__ == '__main__':
    sol = Solution()