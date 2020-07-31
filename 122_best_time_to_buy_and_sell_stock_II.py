class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        
        L = len(prices)
        variation = []
        for i in range(L-1):
            variation.append(prices[i+1]-prices[i])
        


if __name__ == '__main__':
    test1 = [7,1,5,3,6,4]
    sol = Solution()