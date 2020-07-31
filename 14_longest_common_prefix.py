class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        def compare(str1, str2):
            index = 0
            while True:
                try:
                    char1 = str1[index]
                    char2 = str2[index]
                except:
                    break
                if char1 == char2:
                    index += 1
                else:
                    break
            return(str1[:index])


        try:
            common = strs.pop()
        except:
            return('')

        for string in strs:
            common = compare(common, string)
            if common == '':
                break

        return(common)