class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Store nums and target so helper function can use them
        self.nums = nums
        self.target = target
        
        # This will store all valid combinations (final answers)
        self.res = []
        
        # Start DFS:
        # i = 0 → start from first number
        # curr = [] → current combination (nothing chosen yet)
        # total = 0 → sum of current combination
        self.dfs(0, [], 0)
        
        return self.res


    def dfs(self, i, curr, total):
        # ---------------- WHAT IS curr? ----------------
        # curr = the CURRENT COMBINATION we are building
        # Think of it as:
        # → the "path" we have taken so far
        # → the numbers we have chosen up to this point
        #
        # Example during execution:
        # curr = [] → [2] → [2,2] → [2,2,3]
        #
        # total = sum(curr)


        # ---------------- BASE CASE 1 ----------------
        # If total equals target, we found a valid combination
        if total == self.target:
            # IMPORTANT: append a COPY of curr
            # because curr is reused and will change later
            self.res.append(curr.copy())
            return
        
        # ---------------- BASE CASE 2 ----------------
        # Stop exploring if:
        # 1. we used all numbers
        # 2. total exceeds target (invalid path)
        if i >= len(self.nums) or total > self.target:
            return


        # ---------------- CHOICE 1: INCLUDE nums[i] ----------------
        # Add current number to the combination
        curr.append(self.nums[i])

        # Now curr has changed (we "go deeper" in recursion tree)
        # Stay at same index i because we can reuse the same number
        self.dfs(i, curr, total + self.nums[i])

        # ---------------- BACKTRACK ----------------
        # Undo the choice we just made
        # This restores curr to its previous state
        curr.pop()


        # ---------------- CHOICE 2: EXCLUDE nums[i] ----------------
        # Skip current number and move to next index
        self.dfs(i + 1, curr, total)