class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def mode1():
            count = 0
            try:
                while(True):
                    nums.remove(0)
                    count += 1
            except:
                nums[:] = nums+count*[0]


        def mode2():
            L = len(nums)
            count = 0
            i = 0
            while i < L-count-1:
                if nums[i] == 0:
                    nums[i:] = nums[i+1:]+[0]
                    count += 1
                    i -= 1
                i += 1                    


        mode3()