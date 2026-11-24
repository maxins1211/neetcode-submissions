class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        length = len(prices)
        for i in range(length):
            if i < length - 1:
                profit = max(prices[i+1:]) - prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit 