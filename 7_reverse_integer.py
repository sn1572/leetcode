class Solution:
    def reverse(self, x: 'int') -> 'int':

        xString = str(x)
        Max = '2147483647'
        Min = '2147483648'
        
        sign = 1
        out = ''
        if xString[0] == '-':
            sign = -1
            xString = xString[1:]
        
        L = len(xString)
        for i in range(L):
            out = out+xString[L-i-1]

        done = False
        index = 0
        while not done and index < len(xString):
            if out[index] == '0':
                index += 1
            else:
                done = True
        out = out[index:]
        if len(out) == 0:
            return(0)

        maxL = len(Max)
        O = len(out)
        if O > maxL:
            return(0)
        elif O < maxL:
            return(sign*int(out))
        else:
            if sign == 1:
                for i in range(O):
                    if ord(out[i]) > ord(Max[i]):
                        return(0)
                    elif ord(out[i]) < ord(Max[i]):
                        return(sign*int(out))
                return(sign*int(out))
            else:
                for i in range(O):
                    if ord(out[i]) > ord(Min[i]):
                        return(0)
                    elif ord(out[i]) < ord(Min[i]):
                        return(sign*int(out))
                return(sign*int(out))
                

if __name__ == '__main__':
    sol = Solution()
    assert(sol.reverse(101) == 101)
    assert(sol.reverse(120) == 21)
    assert(sol.reverse(-123) == -321)
    assert(sol.reverse(0) == 0)