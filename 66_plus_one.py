class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for digit in digits:
            num += str(digit)
        num = int(num)
        num += 1
        num = str(num)
        out = []
        for digit in num:
            out.append(int(digit))
        return(out)