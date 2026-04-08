class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Result list to store all valid combinations
        self.res = []
        
        # Sort to:
        # 1. Group duplicates together
        # 2. Enable pruning (stop when total > target)
        self.nums = sorted(candidates)
        self.target = target
        
        # Start DFS from index 0
        self.dfs(0, [], 0)
        return self.res
        
    def dfs(self, i, curr, total):
        # ---- BASE CASES ----

        # Found a valid combination
        if total == self.target:
            self.res.append(curr.copy())
            return

        # Stop if:
        # 1. Out of bounds OR
        # 2. Sum exceeded target
        if i >= len(self.nums) or total > self.target:
            return

        # ---- CHOICE 1: TAKE CURRENT ELEMENT ----
        # Include nums[i] in the combination
        curr.append(self.nums[i])

        # Move to next index (each element can only be used once)
        self.dfs(i + 1, curr, total + self.nums[i])

        # Backtrack (remove last added element)
        curr.pop()

        # ---- CHOICE 2: SKIP CURRENT ELEMENT (AND ITS DUPLICATES) ----
        # Skip all duplicate values of nums[i]
        # This prevents generating duplicate combinations
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i += 1

        # Move to next distinct number
        self.dfs(i + 1, curr, total)