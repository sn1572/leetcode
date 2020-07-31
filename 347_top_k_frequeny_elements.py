class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            try:
                counts[num] += 1
            except:
                counts[num] = 1
        counts = sorted(counts.items(), key = lambda item: item[1])
        out = k*[0]
        for i in range(k):
            out[-i-1] = counts[-k+i][0]
        return(out)