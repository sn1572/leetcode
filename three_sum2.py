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
        L = len(self.mergeSortStorage)
        if L == 1:
            a = self.mergeSortStorage[0]
            if a==0:
                if len(self.counts[0]) >= 3:
                    return([[0,0,0]])
            else:
                return([])
        if L == 2:
            a = self.mergeSortStorage[0]
            b = self.mergeSortStorage[1]
            if b+2*a==0 and len(self.counts[a])>1:
                return([[b,a,a]])
            elif a+2*b==0 and len(self.counts[b])>1:
                return([[a,b,b]])
            else:
                return([])
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
        D = self.ind_dict(sub)
        if L==1:
            #This catches two important corner cases:
            #1) There is a cVal c such that -x-c=c.  The solution [x,c,c] can't happen in lists without repetition.
            #2) The case x=0, multiplicity three.
            x = sub[0]
            c=x/2
            if c == int(c):
                try:
                    if len(D[-c])>1:
                        if x<0:
                            self.assign([x, -c, -c])
                        else:
                            self.assign([c,c,x])
                except:
                    pass
        if L==2:
            #check if -sub[0]-sub[1] is in D
            
        M = int((L-1)/2)
        #if L=2, then (L-1)/2 goes to zero, so the while loop doesn't happen
        centerValue = sub[M]
        index = 0
        x = sub[index]
        while index<M:
            try:
                c = -centerValue-x
                if ((c!=x) and (c!=centerValue)):
                    self.assign([-centerValue-x,centerValue,x])
                elif (c==centerValue) and (c != 0) and len(self.counts[c])>1:
                    self.assign([-centerValue-x,centerValue,x])
                elif (c==x) and (c != centerValeu) and len(self.counts[c])>1:
                    self.assign([-centerValue-x,centerValue,x])
                elif (c==x) and (c==centerValue) and len(self.counts[c])>2:
                    self.assign([-centerValue-x,centerValue,x])
            except:
                pass
            
            index += 1
            x=sub[index]
        self.chop(sub[:M])
        self.chop(sub[M:])