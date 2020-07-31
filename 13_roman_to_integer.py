'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        out = 0
        conditional = ['I', 'X', 'C']
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dubs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        index = 0
        L = len(s)
        while index < L:
            char = s[index]
            if char in conditional:
                if index == L-1:
                    out += vals[char]
                    index += 1
                else:
                    chars = s[index:index+2]
                    try:
                        out += dubs[chars]
                        index += 2
                    except:
                        out += vals[char]
                        index += 1
            else:
                out += vals[char]
                index += 1
        return(out)


if __name__ == '__main__':
    test1 = 'III'
    test2 = 'IV'
    test3 = 'IX'
    test4 = 'MCMXCIV'
    test5 = 'LVIII'
    sol = Solution()
    assert(sol.romanToInt(test1) == 3)
    assert(sol.romanToInt(test2) == 4)
    assert(sol.romanToInt(test3) == 9)
    assert(sol.romanToInt(test4) == 1994)
    assert(sol.romanToInt(test5) == 58)