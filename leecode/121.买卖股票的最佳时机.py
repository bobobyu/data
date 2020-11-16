class Solution:
    def maxProfit(self, prices: list) -> int:
        length = len(prices)
        if length <2:
            return 0
        # d = [[0 for i in range(length)] for j in range(length)]
        # d[0] = [prices[i]-prices[0] if  prices[i]-prices[0]> 0 else 0 for i in range(length)]
        #
        # for row in range(1, length):
        #     for col in range(row, length):
        #         # print((prices[col] - prices[row] + d[row-1][row-1], d[row-1][col]))
        #         d[row][col] = max(prices[col] - prices[row] + d[row-1][row-1], d[row-1][col])
        # # [print(i) for i in d]
        # return d[-1][-1]
        profit:int = 0
        for i in range(1, length):
            if prices[i] > prices[i-1]:
                # print(prices[i], prices[i-1])
                profit += prices[i] - prices[i-1]
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
