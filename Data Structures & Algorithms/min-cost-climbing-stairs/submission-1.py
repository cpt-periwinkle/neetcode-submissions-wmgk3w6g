class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo[i] will store:
        # minimum cost to reach the top starting from stair i
        memo = [-1] * len(cost)

        def f(index):
            # Base case:
            # If we are at or beyond the top, no cost is needed
            if index >= len(cost):
                return 0

            # If already computed, reuse it (avoid recomputation)
            if memo[index] != -1:
                return memo[index]

            # Pay cost of current stair, then choose the cheaper path:
            # - go to index + 1
            # - go to index + 2
            memo[index] = cost[index] + min(f(index + 1), f(index + 2))

            return memo[index]

        # We can start from step 0 or step 1
        # So take the cheaper of the two starting points
        return min(f(0), f(1))