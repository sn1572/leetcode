from math import ceil
import bisect


class Solution(object):


    def __init__(self):
        self.maxList = None
        self.backerds = None
        self.maxIndices = None
        self.N = None
        self.height = None


    def getMaxRemaining(self, height):
        N = len(height)
        outMax = N*[0]
        outIndex = N*[0]
        runningMax = height[-1]
        runningIndex = N-1
        outMax[-1] = runningMax
        outIndex[-1] = runningIndex
        for i in range(1,N):
            val = height[N-i-1]
            if val > runningMax:
                runningMax = val
                runningIndex = N-i-1
            outMax[N-i-1] = runningMax
            outIndex = runningIndex
        return([outMax, outIndex])


    def maximize(self, L):
        if L == self.N-2:
            return(min(self.height[L], self.height[self.N-1]))
        valL = self.height[L]
        R = bisect.bisect_left(self.backerds, valL)
        R = self.N-R-1 #Index of furthest right val that is >= valL
        if R <= L:
            R = L+1
        valR = self.height[R]
        maxVal = min(valL, valR)*(R-L)
        if valL <= valR:
            d = 1
            index = ceil(d*(R-L)/(valL-d))
            while index < self.N and d < valL:
                valr, r = self.maxList[R+index], self.maxIndices[R+index]
                if valr >= valL-d:
                    maxVal = valr*(r-L)
                    valR, R = valr, r
                d += 1
                index = ceil(d*(R-L)/(valL-d))
                while index < R and d < valL:
                    d += 1
                    index = ceil(d*(R-L)/(valL-d))
            return(maxVal)
        else:
            d = 1
            index = ceil(d*(R-L)/(valR-d))
            while index < self.N and d < valR:
                valr, r = self.maxList[R+index], self.maxIndices[R+index]
                if valr >= valL-d:
                    maxVal = valr*(r-L)
                    valR, R = valr, r
                d += 1
                index = ceil(d*(R-L)/(valR-d))
                while index < R and d < valR:
                    d += 1
                    index = ceil(d*(R-L)/(valR-d))
            return(maxVal)


    def maxArea(self, height):
        self.maxList, self.maxIndices = self.getMaxRemaining(height)
        self.backerds = self.maxList[::-1]
        self.N = len(height)
        self.height = height


'''
class Solution(object):


    def getMaxRemaining(self, height):
        N = len(height)
        out = N*[0]
        runningMax = height[-1]
        runningIndex = N-1
        out[-1]= [runningMax, runningIndex]
        for i in range(1,N):
            val = height[N-i-1]
            if val > runningMax:
                runningMax = val
                runningIndex = N-i-1
            out[N-i-1] = [runningMax, runningIndex]
        return(out)


    def maximize(self, height, maxList, L):
        N = len(height)
        if L == N-2:
            return(min(height[L], height[N-1]))
        valL = height[L]
        valR, R = maxList[L+1]
        if R < N-1:
            valNext, Next = maxList[R+1]
            while valNext > valL and Next < N-1:
                valR, R = maxList[R+1]
                valNext, Next = maxList[Next+1] 
            if Next == N-1:
                if valNext > valL:
                    valR, R = valNext, Next
        if R == N-1:
            return(min(valR,valL)*(R-L))
        #It should now be the case that valR <= valL
        index = R+1
        maxVal = min(valR,valL)*(R-L)
        while index < N:
            valr, r = maxList[index]
            newVal = valr*(r-L)
            if newVal > maxVal:
                maxVal = newVal
            index = r+1
        return(maxVal)


    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxList = self.getMaxRemaining(height)
        maxVal = -1
        for i in range(len(height)-1):
            newVal = self.maximize(height, maxList, i)
            if newVal > maxVal:
                maxVal = newVal
        return(maxVal)
'''
    

if __name__ == '__main__':
    test = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    print(sol.maxArea(test)) #49
    test2 = [0,2]
    print(sol.maxArea(test2)) #0
    test3 = [5,2,12,1,5,3,4,11,9,4]
    print(sol.maxArea(test3)) #55
    test4 = [10,9,8,7,6,5,4,3,2,1]
    print(sol.maxArea(test4)) #25
    test5 = [4,4,2,11,0,11,5,11,13,8]
    print(sol.maxArea(test5)) #55