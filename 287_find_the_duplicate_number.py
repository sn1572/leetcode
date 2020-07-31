def test(n):
    out = []
    for z in range(1,n):
        out.append([int(n*z-(z**2-z)/2), int((n*(n-1)+z*(z+1))/2)])
    maxOverlap = 0
    maxPair = out[0]
    for i in range(len(out)):
        pair1 = out[i]
        overlaps = 0
        for j in range(i+1, len(out)):
            pair2 = out[j]
            if pair2[0] < pair1[1]:
                overlaps += 1
        if overlaps > maxOverlap:
            maxOverlap = overlaps
            maxPair = pair1
    print(maxOverlap+1)
    print(maxPair)


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        N = len( nums )
        right = N-1
        left_count = 0
        right_count = 0
        mid_count = 0
        mid = (left+right)/2
        while abs( right-left ) >= 0.25:
            mid = (left+right)/2
            for num in nums:
                if num >= left and num < mid:
                    left_count += 1
                elif num > mid and num <= right:
                    right_count += 1
                elif num == mid:
                    mid_count += 1
            if mid_count > 1:
                print("mid > 1")
                #return( round( mid ) )
            if left_count > right_count:
                right = mid
            else:
                left = mid
            left_count = 0
            right_count = 0
            mid_count = 0
        return( round( mid ) )


if __name__ == '__main__':
    #nums = [3,1,3,4,2]
    #nums = [1,1,2]
    #nums = [1,3,4,2,2]
    #nums = [1,2,3,4,1]
    nums = [8,1,1,9,5,4,2,7,3,6]
    #nums = [1,1]
    sol = Solution()
    print(sol.findDuplicate(nums))