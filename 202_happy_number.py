class Solution:
    def isHappy(self, n: 'int') -> 'bool':

        seen = {}
        while True:
            digits = str(n)
            newVal = 0
            L = len(digits)
            for i in range(L):
                newVal += int(digits[i])**2
            if newVal == 1:
                return(True)
            try:
                seen[newVal] += 1
                return(False)
            except:
                seen[newVal] = 1
            n = newVal