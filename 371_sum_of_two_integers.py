class Solution:
    def getSum(self, a: 'int', b: 'int') -> 'int':


        def addBits(bit1, bit2, carry):
            #returns (val, carry)
            if bit1 == bit2 == '1':
                if carry == '0':
                    return('0','1')
                elif carry == '1':
                    return('1','1')
            elif bit1 == bit2 == '0':
                if carry == '0':
                    return('0','0')
                elif carry == '1':
                    return('1','0')
            else:
                if carry == '0':
                    return('1','0')
                else:
                    return('0','1')


        def determineBit(bit1, result, carry):
            #Given bit1, the result, and carry,
            #determines the bit X and the carry
            #value newCarry that satisfy the relation
            #result, newCarry = addBits(bit1, X, carry).
            #Return value is (X, newCarry)
            if bit1 == carry == '1':
                if result == '0':
                    return('0', '1')
                if result == '1':
                    return('1', '1')
            elif bit1 == carry == '0':
                if result == '0':
                    return('0', '0')
                if result == '1':
                    return('1', '0')
            else:
                if result == '0':
                    return('1', '1')
                if result == '1':
                    return('0', '0')


        def addBinWords(x, y):
            #Assumes both words x and y are the same length.
            carry = '0'
            added = ''
            L = len(x)
            for i in range(L):
                val, carry = addBits(x[L-i-1], y[L-i-1], carry)
                added = val+added
            if carry == '1':
                added = '1'+added
            return(added)


        def subtractBinWords(x, y):
            #Assumes both words x and y are the same length,
            #and y < x.
            carry = '0'
            result = ''
            L = len(x)
            for i in range(L):
                val, carry = determineBit(x[L-i-1], y[L-i-1], carry)
                result = val+result
            if carry == '1':
                result = '1'+result
            return(result)


        sign_x, x = bin(a).split('b')
        sign_y, y = bin(b).split('b')
        len_x = len(x)
        len_y = len(y)

        if len_x >= len_y:
            y = (len_x-len_y)*'0'+y
            #ensures that len_x = len_y.
        else:
            x = (len_y-len_x)*'0'+x

        if sign_x == sign_y:
            added = addBinWords(x,y)
            if sign_x == '-0':
                return(-int(added, 2))
            else:
                return(int(added, 2))
        else:
            if abs(a) >= abs(b):
                result = subtractBinWords(y, x)
                if sign_x == '-0':
                    return(-int(result, 2))
                else:
                    return(int(result, 2))
            else:
                result = subtractBinWords(x, y)
                if sign_x == '-0':
                    return(int(result, 2))
                else:
                    return(-int(result, 2))


if __name__ == '__main__':
    sol = Solution()
    assert(sol.getSum(4, 5) == 9)
    assert(sol.getSum(0, 10) == 10)
    assert(sol.getSum(4, -5) == -1)
    assert(sol.getSum(-3,-2) == -5)
    assert(sol.getSum(0, 0) == 0)
    assert(sol.getSum(-0, 0) == 0)
    assert(sol.getSum(-0, -0) == 0)
                