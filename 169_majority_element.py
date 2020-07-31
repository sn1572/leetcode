class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        counts = {}
        for element in nums:
            try:
                counts[element] += 1
            except:
                counts[element] = 1
        L = len(nums)
        for num, count in counts.items():
            if count > L/2:
                return(num)