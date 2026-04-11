class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: # Top Down Tabular DP
        n = len(cost)
        table = [0] * (n + 1)

        for i in range(2, n + 1):
            table[i] = min((table[i - 1] + cost[i - 1]), (table[i - 2] + cost[i - 2]))

        return table[n]