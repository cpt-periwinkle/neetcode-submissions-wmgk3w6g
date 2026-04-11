class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
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

