# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:10:10 2019

@author: mbolding3
"""


class Solution:


    def findMinimals(self, s):
        # BFS stage, finds indices of all palindromes
        # of length 2 or 3
        len2, len3 = [], []
        N = len(s)
        for i in range(N-1):
            if s[i] == s[i+1]:
                len2.append(i)
            if i <= N-3 and s[i] == s[i+2]:
                len3.append(i+1)
        return(len2, len3)


    def DFS(self, s, index, kind):
        # creates list of all palindrome indices containing 
        # the minimal palindrome beginning at index.
        if kind == 2:
            # search for palindromes of the types 'aa...a' or 'baab'
            out = [(index, index+1)]
            left = index
            right = index+1
            while left > 0:
                left -= 1
                if s[left] == s[right]:
                    out.append((left, right))
                else:
                    break
            left = index
            while right < len(s)-1:
                right += 1
                if s[right] == s[left]:
                    out.append((left, right))
                else:
                    break
            right = index+1
        else:
            out = [(index-1, index+1)]
            # search for palindromes of the type 'aba'
            left = index-1; right = index+1

        while left > 0 and right < len(s)-1:
            left -= 1; right += 1
            if s[right] == s[left]:
                out.append((left, right))
            else:
                break

        return(out)


    def generateAllPartitions(self, s):
        len2, len3 = self.findMinimals(s)
        palindromeIndices = dict([])
        for i in len2:
            for a, b in self.DFS(s, i, 2):
                if a in palindromeIndices:
                    palindromeIndices[a].add(b)
                else:
                    palindromeIndices[a] = set([b])
        for i in len3:
            for a, b in self.DFS(s, i, 3):
                if a in palindromeIndices:
                    palindromeIndices[a].add(b)
                else:
                    palindromeIndices[a] = set([b])
        for i in range(len(s)):
            if i in palindromeIndices:
                palindromeIndices[i].add(i)
            else:
                palindromeIndices[i] = set([i])
        # palindromeIndices now contains all the possible palindromes inside s.
        return(palindromeIndices)


    def listPartitions(self, index):
        if index not in self.palindromeIndices:
            return([[]])
        out = []
        for index2 in self.palindromeIndices[index]:
            for array in self.listPartitions(index2+1):
                out.append([self.s[index:index2+1]]+array)
        return(out)


    def partition(self, s):
        self.s = s
        self.palindromeIndices = self.generateAllPartitions(s)
        if len(s) == 1:
            return([[s]])
        elif not s:
            return([])
        return(self.listPartitions(0))


if __name__ == '__main__':
    sol = Solution()
    #test = 'aabaaabaa'
    test = 'aab'
    print(sol.partition(test))