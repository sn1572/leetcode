class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = []
        L = len(s)
        for i in range(L):
            char = s[i]
            if char in ['(', '[', '{']:
                opened.append(char)
            else:
                try:
                    last = opened.pop()
                except:
                    return(False)
                if last == '(':
                    if char in [']', '}']:
                        return(False)
                elif last == '[':
                    if char in [')', '}']:
                        return(False)
                else:
                    if char in [')', ']']:
                        return(False)
        try:
            opened.pop()
            return(False)
        except:
            return(True)