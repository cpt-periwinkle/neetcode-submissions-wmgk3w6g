class Solution:
    def rob(self, nums: List[int]) -> int:  # Recursive + Memoization
        
        # memo[i] stores:
        # maximum money we can rob starting from house i
        memo = [-1] * len(nums)

        def dfs(i):
            # Base case:
            # If we go beyond the last house, no money can be collected
            if i >= len(nums):
                return 0

            # If we already solved this subproblem, reuse it
            if memo[i] != -1:
                return memo[i]

            # Choice 1: Pick this house
            # Take its value, then skip next house (i + 1)
            pick = nums[i] + dfs(i + 2)

            # Choice 2: Skip this house
            # Move to the next house
            skip = dfs(i + 1)

            # Store the best of both choices
            memo[i] = max(pick, skip)

            return memo[i]

        # Start from house 0
        return dfs(0)