class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases
        if len(nums) == 1:
            return nums[0]

        # Two cases:
        # 1. Skip first house
        # 2. Skip last house
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums):
        # Handle small cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            skip = prev1
            pick = prev2 + nums[i]
            prev1 = max(skip, pick)
            prev2 = skip

        return prev1