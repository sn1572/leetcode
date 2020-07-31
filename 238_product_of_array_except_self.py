class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fore_tot = nums[0]
        aft_tot = nums[-1]
        L = len(nums)
        fore = L*[0]
        aft = L*[0]
        fore[0] = fore_tot
        aft[-1] = aft_tot
        for i in range(1,L):
            fore_tot *= nums[i]
            aft_tot *= nums[-i-1]
            fore[i] = fore_tot
            aft[-i-1] = aft_tot
        out = []
        out.append(aft[1])
        for i in range(1,L-1):
            out.append(fore[i-1]*aft[i+1])
        out.append(fore[-2])
        return(out)


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([1,2]))