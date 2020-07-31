class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        D = self.ind_dict(nums)
        solution = []
        L = len(nums)
        for i in range(L):
            for j in range(i+1,L):
                a=nums[i]; b=nums[j]
                try:
                    c=-a-b
                    k = max(D[c])
                    if k>j:
                        sol = [a,b,c]
                        if self.not_in_list(solution, sol):
                            solution.append(sol)
                except:
                    pass
        return(solution)
        
    def ind_dict(self, array):
        D={}
        for i in range(len(array)):
            try:
                D[array[i]].append(i)
            except:
                D[array[i]] = [i]
        return(D)
        
    def faster_same(self, list1, list2):
        if set(list1) == set(list2):
            return(True)
        else:
            return(False)
            
    def quick_same(self, list1, list2):
        m1=0; m2=0
        for i in range(3):
            a = list1[i]; b= list2[i]
            m1 += a**2
            m2 += b**2
        if (m1 == m2):
            return(True)
        else:
            return(False)
        
    def same(self, list1, list2):
        a = list1[0]; b = list1[1]; c = list1[2]
        if ((a in list2) and (b in list2) and (c in list2)):
            a = list2[0]; b = list2[1]; c = list2[2]
            if ((a in list1) and (b in list1) and (c in list1)):
                return(True)
        else:
            return(False)
            
    def not_in_list(self, array, target):
        for element in array:
            if self.quick_same(element, target):
                return(False)
        return(True)