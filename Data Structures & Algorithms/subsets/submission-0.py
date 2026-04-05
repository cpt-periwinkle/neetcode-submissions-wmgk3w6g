class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subsetsRecursive(0, nums, [])
        return self.res

    def subsetsRecursive(self, idx, nums, arr):
        if (idx >= len(nums)):
            self.res.append(arr[:])
            return
        arr.append(nums[idx])
        self.subsetsRecursive(idx + 1, nums, arr)
        arr.pop()
        self.subsetsRecursive(idx + 1, nums, arr)