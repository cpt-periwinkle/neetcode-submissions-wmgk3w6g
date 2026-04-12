class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Total sum of array
        total = sum(nums)
        
        # If total is odd, we cannot split into two equal subsets
        if total % 2 != 0:
            return False
        
        # We now just need to find a subset with sum = total // 2
        target = total // 2

        # memo[(i, target)] = whether we can form 'target' using nums[i:]
        memo = {}

        def dfs(i, target):
            # If we hit exactly 0, we successfully formed the subset
            if target == 0:
                return True

            # If we run out of elements OR overshoot target → invalid path
            if i >= len(nums) or target < 0:
                return False

            # If we've already solved this state, reuse result
            if (i, target) in memo:
                return memo[(i, target)]

            # Choice 1: skip current number
            # Choice 2: take current number (reduce target)
            memo[(i, target)] = (
                dfs(i + 1, target) or 
                dfs(i + 1, target - nums[i])
            )

            return memo[(i, target)]

        # Start from index 0 trying to build 'target'
        return dfs(0, target)