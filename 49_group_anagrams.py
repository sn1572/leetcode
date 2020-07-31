#from functools import reduce


class Solution(object):


    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.primes += [31, 37, 41, 43, 47, 53, 59, 61, 67]
        self.primes += [71, 73, 79, 83, 89, 97, 101]


    def toNum(self, string):
        #return(reduce(lambda x,y: ord(x)+ord(y) if type(x) == str else x+ord(y), string))
        total = 1
        for char in string:
            total *= self.primes[ord(char)-ord('a')]
        return(total)


    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        hashes = list(map(self.toNum, strs))
        for i in range(len(hashes)):
            num = hashes[i]
            if num in anagrams:
                anagrams[num] += [strs[i]]
            else:
                anagrams[num] = [strs[i]]
        return(list(anagrams.values()))


if __name__ == '__main__':
    test = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(test))


'''
def toNum(string):
        total = 1
        for char in string:
            total *= ord(char)
        return(total)
'''