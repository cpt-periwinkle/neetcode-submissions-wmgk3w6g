class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        return True
        