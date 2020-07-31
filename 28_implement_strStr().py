class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


        def compare(word1, word2):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    return(False)
            return(True)


        if needle == '':
            return(0)

        lHay = len(haystack)
        lNeed = len(needle)

        if lHay < lNeed:
            return(-1)

        for i in range(lHay-lNeed+1):
            if compare(haystack[i:i+lNeed], needle):
                return(i)

        return(-1)