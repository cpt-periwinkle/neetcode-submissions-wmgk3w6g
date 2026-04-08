class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs(0, [])
        return self.res


    def dfs(self, i, curr):
        if i >= len(self.nums):
            self.res.append(curr.copy())
            return
        
        curr.append(self.nums[i])
        self.dfs(i + 1, curr)
        curr.pop()
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i += 1
        self.dfs(i + 1, curr)