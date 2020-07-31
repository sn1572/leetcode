class Solution(object):


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #The following works:
        #L = len(nums)
        #k = k % L
        #nums[:] = nums[-k:]+nums[:-k]

        L = len(nums)
        k = k % L
        if k:
            for i in range(L//k):
                for j in range(k):
                    nums[k*i+j], nums[-k+j] = nums[-k+j], nums[k*i+j]
            #After this procedure, the last L % k elements of nums
            #will be equal to rotate(nums[:L%k], k-L%k). Therefore we
            #need to "unrotate" these.
            try:
                k, L = k-L%k, L%k
                k = k % L
                if k:
                    for i in range(L//k):
                        for j in range(k):
                            nums[k*i+j-L], nums[-k+j] = nums[-k+j], nums[k*i+j-L]
            except:
                pass


if __name__ == '__main__':
    test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    test2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    sol = Solution()
    sol.rotate(test2,11)
    print(test2)