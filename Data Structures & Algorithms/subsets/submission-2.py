class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, curr):
            if idx >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            dfs(idx + 1, curr)
            curr.pop()
            dfs(idx + 1, curr)

        dfs(0, [])
        return res