class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:  # Bottom-up DP
        n = len(cost)

        # table[i] = minimum cost to reach step i
        # Step n is the "top" (no cost associated with it)
        table = [0] * (n + 1)

        # We start at step 0 or step 1 for free
        # So:
        # table[0] = 0
        # table[1] = 0
        # (already initialized)

        # Build the solution from smaller steps to larger steps
        for i in range(2, n + 1):
            # To reach step i, we must come from:
            # - step i-1 (taking 1 step)
            # - step i-2 (taking 2 steps)

            # If we come from i-1:
            # cost = cost to reach (i-1) + cost of stepping on (i-1)
            one_step = table[i - 1] + cost[i - 1]

            # If we come from i-2:
            # cost = cost to reach (i-2) + cost of stepping on (i-2)
            two_steps = table[i - 2] + cost[i - 2]

            # Choose the cheaper of the two ways
            table[i] = min(one_step, two_steps)

        # table[n] = minimum cost to reach the top
        return table[n]