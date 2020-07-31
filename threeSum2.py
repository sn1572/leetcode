class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        D = self.ind_dict(nums)
        solution = {}
        op = self.mergeSort(list(D.keys())) #remove all duplicates from nums
        #chop assumes that the input is sorted and without repeats
        self.chop(op)
        return(solution.keys())
        
    def ind_dict(self, array):
        D={};
        for i in range(len(array)):
            try:
                D[array[i]].append(i)
            except:
                D[array[i]] = [i]
        return(D)
                
    def mergeSort(self, array):
        #note this mergesort is catered to arrays with no duplicates
        L = len(array)
        if L==1:
            return(array)
        elif L==2:
            a=array[0]; b=array[1]
            if a>b:
                return([b,a])
            else:
                return(array)
        M = int(L/2)
        left = self.mergeSort(array[:M])
        right = self.mergeSort(array[M:])
        return(self.merge(left, right))
        
    def merge(self, left, right):
        #as noted above, we assume that left and right have no common elements
        leftIndex = 0
        rightIndex = 0
        R = len(right)
        L = len(left)
        merged = []
        while leftIndex<L:
            while rightIndex < R and left[leftIndex]>right[rightIndex]:
                merged.append(right[rightIndex])
                rightIndex += 1
            merged.append(left[leftIndex])
            leftIndex += 1
        if rightIndex < R:
            merged = merged+right[rightIndex:]
        if leftIndex < L:
            merged = merged+left[leftIndex:]
        return(merged)
    
    def chop(self, sub):
        global D, solution
        L = len(sub)
        if L < 3:
            return(None)
        maxm = sub[-1]
        minm = sub[0]
        try:
            unused = D[-maxm-minm]
            M = maxm-minm
            index = 0
            x = sub[index]
            while x<M/2:
                try:
                    unused = D[M-x]
                    try:
                        unused = solution[str([M-x,x,-maxm-minm])]
                    except:
                        solution[str([M-x,x,-maxm-minm])] = 1
                except:
                    pass
                index += 1
                x=sub[index]
            if x==M/2:
                if len(D[x])>1:
                    try:
                        unused = solution[str([M-x,x,-maxm-minm])]
                    except:
                        solution[str([M-x,x,-maxm-minm])] = 1
        except:
            pass
        m = int((-maxm-minm)/2)
        self.chop(sub[:m])
        self.chop(sub[m:])