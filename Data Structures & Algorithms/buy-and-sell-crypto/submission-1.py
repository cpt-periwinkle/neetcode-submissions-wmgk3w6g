class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:        # This helps us find the local minimum in the elements seen till then
                left = right                        # We want to buy on the cheapest day
            else:
                profit = prices[right] - prices[left]   # if there is a price which is good to sell, only then this condition applies
                max_profit = max(max_profit, profit)
        
        return max_profit   # will be set to default zero in case the above else condition is never hit
            