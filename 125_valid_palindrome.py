class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return(True)

        charList = []
        for char in s:
            char = char.lower()
            val = ord(char)
            if val >= ord('0') and val <= ord('9'):
                charList.append(char)
            elif val >= ord('a') and val <= ord('z'):
                charList.append(char)

        length = len(charList)
        left = int(length/2)
        for i in range(left):
            if charList[-i-1] != charList[i]:
                return(False)

        return(True)