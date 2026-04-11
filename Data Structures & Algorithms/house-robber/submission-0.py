class Solution:
    def rob(self, nums: List[int]) -> int: # Recursive
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != (-1):
                return memo[i]
            pick = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)
            memo[i] = max(pick, skip)
            return memo[i]

        return dfs(0)