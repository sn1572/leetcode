class Solution:
    def __init__(self):
        self.solution = {}
        self.counts = {}
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.counts = self.ind_dict(nums)
        op = self.mergeSort(list(self.counts.keys())) #remove all duplicates from nums
        #chop assumes that the input is sorted and without repeats
        self.chop(op)
        return(list(self.solution.values()))
        
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
        
    def assign(self, array):
        try:
            unused = self.solution[str(array)]
        except:
            self.solution[str(array)] = array
        
    def addSolution(self,a,b,c):
        if a>b:
            if c>a:
                self.assign([c,a,b])
            elif c>b:
                self.assign([a,c,b])
            else:
                self.assign([a,b,c])
        else:
            if c>b:
                self.assign([c,b,a])
            elif c>a:
                self.assign([b,c,a])
            else:
                self.assign([b,a,c])
    
    def chop(self, sub):
        L = len(sub)
        if L < 3:
            return(None)
        if L==3:
            a=sub[0]; b=sub[1]; c=sub[2]
            if a+b+c == 0:
                self.addSolution(a,b,c)
            return(None)
        M = int(L/2)
        D = self.ind_dict(sub)
        centerValue = sub[M]
        index = 0
        x = sub[index]
        while index<M and x<=0:
            x = sub[index]
            try:
                unused = D[-centerValue-x]
                self.assign([-centerValue-x,centerValue,x])
            except:
                pass
            if len(self.counts[x])>1:
                try:
                    y = -2*x
                    unused = D[y]
                    self.assign([y,x,x])
                except:
                    pass
            index += 1
            x=sub[index]
        c = centerValue/2
        if c == int(c):
            try:
                if len(D[-c])>1:
                    if centerValue>0:
                        self.assign([centerValue, -c, -c])
                    else:
                        self.assign([c,c,centerValue])
            except:
                pass
        self.chop(sub[:M])
        self.chop(sub[M:])