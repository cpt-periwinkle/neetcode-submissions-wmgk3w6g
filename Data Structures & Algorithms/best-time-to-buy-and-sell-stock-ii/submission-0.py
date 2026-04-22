class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through the prices -> Take the current min as the first index
            # as we go through, we see if anything is more than the current minimum
            # if yes, we add add the difference to a variable profit
            # then we set the minimum to the current index and repeat the process!

        maxProfit = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > 0:
                    left = right
                    maxProfit += profit
        
        return maxProfit