class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: # Space Optimized Top Down DP
        # prev2 = minimum cost to reach step i - 2
        # prev1 = minimum cost to reach step i - 1
        prev2 = 0
        prev1 = 0

        # Build from step 2 up to the top
        for i in range(2, len(cost) + 1):
            # To reach step i:
            # - come from i - 1 and pay cost[i - 1]
            # - or come from i - 2 and pay cost[i - 2]
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])

            # Shift the window forward
            prev2 = prev1
            prev1 = curr

        # prev1 now stores the minimum cost to reach the top
        return prev1