# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:03:01 2019

@author: mbolding3
"""

class Solution:


    keys = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


    def letterCombinations(self, digits, first = True):

        if first:
            no1 = ''
            for num in digits:
                if num is not '1':
                    no1 += num
            digits = no1
            if digits == '':
                return[]

        num = digits[0]
        leftover = digits[1:]
        if leftover:
            leftover = self.letterCombinations(leftover, False)
        else:
            return(list(self.keys[num]))
        out = []
        for letter in self.keys[num]:
            out += list(map(lambda x: letter+x, leftover))
        return(out)


if __name__ == '__main__':
    sol = Solution()
    test = '1421'
    print(sol.letterCombinations(test))