class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array so duplicates are adjacent
        # This is crucial for skipping duplicates cleanly
        nums.sort()
        self.nums = nums
        self.res = []

        # Start DFS from index 0 with an empty subset
        self.dfs(0, [])
        return self.res


    def dfs(self, i, curr):
        # Base case:
        # If we've considered all elements, record the current subset
        if i >= len(self.nums):
            self.res.append(curr.copy())
            return
        
        # ---- CHOICE 1: TAKE current element ----
        # Include nums[i] in the subset
        curr.append(self.nums[i])

        # Move to next index
        self.dfs(i + 1, curr)

        # Backtrack (remove last element)
        curr.pop()

        # ---- CHOICE 2: SKIP current element (AND ITS DUPLICATES) ----
        # If we decide NOT to take nums[i],
        # we must skip all identical values to avoid duplicate subsets
        #
        # Example:
        # nums = [1,2,2]
        # If we skip the first '2', we should also skip the next '2'
        # otherwise we generate duplicate subsets like [1,2]
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i += 1

        # Move to next distinct element
        self.dfs(i + 1, curr)