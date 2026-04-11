class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # table[i] = max money we can rob from houses 0 to i
        table = [0] * len(nums)

        # Base cases:
        # If only first house → take it
        table[0] = nums[0]

        # For second house:
        # Either take first or second, whichever is larger
        table[1] = max(nums[0], nums[1])

        # Build the solution from left to right
        for i in range(2, len(nums)):
            # Choice 1: Skip current house
            # → take best till previous house
            skip = table[i - 1]

            # Choice 2: Rob current house
            # → take current value + best till i-2
            pick = table[i - 2] + nums[i]

            # Choose the better of the two
            table[i] = max(skip, pick)

        # Last index contains the maximum we can rob
        return table[-1]