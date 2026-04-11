class Solution:
    def climbStairs(self, n: int) -> int: # Space Optimized DP
        # Base cases:
        # 1 step → 1 way
        # 2 steps → 2 ways
        if n <= 2:
            return n

        prev = 1  # ways to reach step 1 (i - 2)
        curr = 2  # ways to reach step 2 (i - 1)

        # Build from step 3 up to n
        for _ in range(3, n + 1):
            next_val = prev + curr  # ways(i) = ways(i-1) + ways(i-2)

            # Shift forward:
            # prev becomes old curr (i-1)
            # curr becomes new value (i)
            prev = curr
            curr = next_val

        # curr now holds ways to reach step n
        return curr