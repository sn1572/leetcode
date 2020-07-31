class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        record = {}
        for num in nums:
            try:
                record.pop(num)
            except:
                record[num] = 1
        return(list(record.keys())[0])