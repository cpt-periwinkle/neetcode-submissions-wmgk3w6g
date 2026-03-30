class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        soln_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in soln_map:
                return [soln_map[complement], i]
                
            soln_map[nums[i]] = i