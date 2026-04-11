class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases:
        # f(0) = 1 → one way to stay at ground (do nothing)
        # f(1) = 1 → [1]
        # f(2) = 2 → [1+1], [2]
        memo = {0: 1, 1: 1, 2: 2}

        def f(x):
            # If we have already computed this, return it
            if x in memo:
                return memo[x]

            # Recurrence:
            # ways to reach x = ways to reach (x-1) + ways to reach (x-2)
            memo[x] = f(x - 1) + f(x - 2)

            return memo[x]

        # Compute number of ways to reach step n
        return f(n)