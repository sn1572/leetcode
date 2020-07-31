class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string = bin(n)[2:]
        index = 0
        total = 0
        while string != '':
            if string[0] == '1':
                total += 2**index
            index += 1
            string = string[1:]
        return(total*2**(32-index))