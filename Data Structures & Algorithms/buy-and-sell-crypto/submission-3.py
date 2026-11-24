class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < length:
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right = left + 1
            if profit >= 0:
                right += 1
            if profit > max_profit:
                max_profit = profit
        return max_profit