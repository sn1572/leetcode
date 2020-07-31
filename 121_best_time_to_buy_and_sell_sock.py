class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':

        L = len(prices)
        if L == 0:
            return(0)
        maximum = prices[-1]
        maxProfit = 0

        for i in range(L):
            val = prices[L-i-1]
            if val > maximum:
                maximum = val
            profit = maximum-val
            if profit > maxProfit:
                maxProfit = profit
            

        return(maxProfit)


if __name__ == '__main__':
    sol = Solution()
    assert(sol.maxProfit([7,1,5,3,6,4]) == 5)