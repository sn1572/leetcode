class Solution:
    def __init__(self):
        self.solution = {}
        self.counts = {}
        self.mergeSortStorage = []
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return([])
        self.solution = {}
        self.counts = self.ind_dict(nums)
        self.mergeSort(list(self.counts.keys())) #remove all duplicates from nums
        #chop assumes that the input is sorted and without repeats
        self.chop(self.mergeSortStorage)
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
        self.mergeSortStorage = []
        index = 0
        L = len(array)
        while index < L:
            chunk = array[index:index+2]
            ell = len(chunk)
            if ell==2:
                a=chunk[0]; b=chunk[1]
                if a>b:
                    self.mergeSortStorage.append([b,a])
                else:
                    self.mergeSortStorage.append(chunk)
            index += 2
        if L%2 != 0:
            self.mergeSortStorage.append([array[-1]])
        while len(self.mergeSortStorage)>1:
            hold = []
            index = 0
            length = len(self.mergeSortStorage)
            while index < length-1:
                left = self.mergeSortStorage[index]
                right = self.mergeSortStorage[index+1]
                hold.append(self.merge(left, right))
                index += 2
            if length%2 != 0:
                hold.append(self.mergeSortStorage[index])
            self.mergeSortStorage = hold
        self.mergeSortStorage = self.mergeSortStorage[0]
        
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
        
    def getIndex(self, x, array):
        copy = array[:]; index = 0
        left = 0; right = len(copy)-1
        if x<copy[left] or x>copy[right]:
            return(-1)
        while True:
            L = len(copy)
            left = 0; right = L-1
            midP = int((left+right)/2)
            if right == 0:
                y = copy[0]
                if x == y:
                    return(index)
                elif x>y:
                    return(index+1)
                else:
                    return(index)
            if right == 1:
                midP=1
            midV = copy[midP]
            if x == midV:
                return(index+midP)
            elif x>midV:
                copy = copy[midP:]
                index += midP
            elif x<midV:
                copy = copy[:midP]
        
    def assign(self, array):
        try:
            unused = self.solution[str(array)]
        except:
            self.solution[str(array)] = array
        
    def order(self,a,b,c):
        if a>b:
            if c>a:
                return([c,a,b])
            elif c>b:
                return([a,c,b])
            else:
                return([a,b,c])
        else:
            if c>b:
                return([c,b,a])
            elif c>a:
                return([b,c,a])
            else:
                return([b,a,c])
                
    def checkSolution(self,x,centerValue):
        try:
            c = -centerValue-x
            unused = self.counts[c]
            ordered = self.order(c,centerValue,x)
            a1 = ordered[0]; a2 = ordered[1]; a3 = ordered[2]
            if a1 > a2:
                if a2>a3:
                    self.assign(ordered)
                elif len(self.counts[a2])>1:
                        self.assign(ordered)
            elif len(self.counts[a1])>1:
                if a2>a3:
                    self.assign(ordered)
                elif len(self.counts[a1])>2:
                    self.assign(ordered)
        except:
            pass
    
    def chop(self, sub):
        L = len(sub)
        if L >= 2:
            leftVal = sub[0]; rightVal = sub[L-1]
            if leftVal <= 0 and rightVal <= 0:
                return(None)
            elif leftVal >= 0 and rightVal >= 0:
                return(None)
            M = self.getIndex(-leftVal-rightVal, sub)
        #at this point, you know that leftVal < 0 and rightVal > 0.
        
            if M == -1:
                print(str(sub)+" M=-1.")
                if -leftVal-rightVal < leftVal:
                    print("too negative")
                    self.chop(sub[:-1])
                else:
                    print("too positive")
                    self.chop(sub[1:])
                return(None)
            elif M == 0:
                self.chop(sub[:1])
                self.chop(sub[1:])
                return(None)
        if L==1:
            print(str(sub)+" L==1.")
            x = sub[0]
            c=x/2
            if c == int(c):
                c = int(c)
                self.checkSolution(x,-c)
            return(None)
        elif L==2:
            print(str(sub)+" L==2.")
            self.checkSolution(sub[0], sub[1])
            self.chop(sub[:1])
            self.chop(sub[1:])
        else:
            print(str(sub)+" L>2.")
            centerValue = sub[M]
            index = 0
            x = sub[index]
            while index < M:
                self.checkSolution(x, centerValue)
                index += 1
                x=sub[index]
            self.chop(sub[:M])
            self.chop(sub[M:])