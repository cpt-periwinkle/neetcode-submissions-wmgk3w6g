class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        return max_profit