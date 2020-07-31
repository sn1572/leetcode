class Solution:
    def titleToNumber(self, s: 'str') -> 'int':

        
        def getVal(char):
            return(ord(char)-ord('A')+1)
            
            
        out = 0
        L = len(s)
        for i in range(L):
            character = s[L-i-1]
            out += getVal(character)*26**i
        return(out)