class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 0:
            return(0)
        elif L == 1:
            return(1)
        index = 1
        for i in range(1,L):
            if nums[i] != nums[index-1]:
                nums[index] = nums[i]
                index += 1
        return(index)


if __name__ == '__main__':
    sol = Solution()
    test1 = [0,0,1,1,1,2,2,3,3,4]
    assert(sol.removeDuplicates(test1) == 5)