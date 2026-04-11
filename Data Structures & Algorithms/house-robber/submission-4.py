class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases:
        # No houses → no money
        if not nums:
            return 0

        # Only one house → must rob it
        if len(nums) == 1:
            return nums[0]

        # prev2 = max money we can rob from houses [0 .. i-2]
        # prev1 = max money we can rob from houses [0 .. i-1]
        prev2 = nums[0]

        # For first two houses:
        # Either take house 0 or house 1 (cannot take both)
        prev1 = max(nums[0], nums[1])

        # Iterate through remaining houses
        for i in range(2, len(nums)):

            # Choice 1: Skip current house
            # → take best we had till previous house
            skip = prev1

            # Choice 2: Rob current house
            # → add current value to best till i-2 (since we skip adjacent)
            pick = prev2 + nums[i]

            # Decide the better option for current position
            prev1 = max(skip, pick)

            # Move the window forward:
            # prev2 should now represent dp[i-2] for next iteration
            # which is the old dp[i-1] (stored in skip)
            prev2 = skip

        # prev1 now holds the maximum money for entire array
        return prev1