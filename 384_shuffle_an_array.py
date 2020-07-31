import random


class Solution(object):


    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.N = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return(self.nums)
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        randShuffling = self.N*[0]
        usableVals = self.nums[:]
        for i in range(self.N):
            pointer = random.randint(0,self.N-i-1)
            randShuffling[i] = usableVals[pointer]
            del usableVals[pointer]
        return(randShuffling)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == '__main__':
    sol = Solution([1,2,3,4,5])