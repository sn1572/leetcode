class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pointers = [[None,None],[None,None],[None,None]]
        #order is: L0, R0, L1, R1, L2, R2
        i = 0
        while i < len(nums):
            color = nums[i]
            if color == 2:
                pointers[2][1] = i
                if pointers[2][0] == None:
                    pointers[2][0] = i
            elif color == 1:
                left2, right2 = pointers[2]
                if left2 is not None:
                    nums[left2], nums[i] = nums[i], nums[left2]
                    pointers[2][0] += 1
                    pointers[2][1] += 1
                    try:
                        pointers[1][1] += 1
                    except:
                        pointers[1][0] = pointers[1][1] = left2
                else:
                    try:
                        pointers[1][1] += 1
                    except:
                        pointers[1][0] = pointers[1][1] = i
            else:
                left1, right1 = pointers[1]
                if left1 is not None:
                    nums[left1], nums[i] = nums[i], nums[left1]
                    pointers[1][0] += 1
                    pointers[1][1] += 1
                    try:
                        pointers[0][1] += 1
                    except:
                        pointers[0][0] = pointers[0][1] = 0
                left2, right2 = pointers[2]
                if left2 is not None:
                    color = nums[i]
                    nums[left2], nums[i] = nums[i], nums[left2]
                    pointers[2][0] += 1
                    pointers[2][1] += 1
                    try:
                        pointers[color][1] += 1
                    except:
                        if color == 0:
                            pointers[0][0] = pointers[0][1] = 0
                        else:
                            pointers[1][0] = pointers[1][1] = left2
            i += 1


if __name__ == '__main__':
    sol = Solution()
    test = [2,0,2,1,1,0]
    sol.sortColors(test)
    print(test)