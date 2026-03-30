class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 'left' represents the day we buy (candidate for minimum price)
        # 'right' represents the day we sell
        left = 0

        # Tracks the maximum profit seen so far
        max_profit = 0

        # Iterate through prices using the 'right' pointer
        for right in range(1, len(prices)):

            # If we find a lower price, update 'left' (better day to buy)
            # This ensures we always buy at the lowest price seen so far
            if prices[left] > prices[right]:
                left = right

            else:
                # Calculate profit if selling on 'right' day
                profit = prices[right] - prices[left]

                # Update maximum profit if this is better
                max_profit = max(max_profit, profit)

        # If no profitable transaction exists, max_profit remains 0
        return max_profit