class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This will store all subsets
        self.res = []

        # Start recursion from index 0 with an empty subset
        self.subsetsRecursive(0, nums, [])

        return self.res


    def subsetsRecursive(self, idx, nums, arr):
        # BASE CASE:
        # If we've processed all elements, store the current subset
        if idx >= len(nums):
            # IMPORTANT: append a COPY, not arr itself (arr keeps changing)
            self.res.append(arr.copy())
            return

        # ---------------- CHOICE 1: INCLUDE nums[idx] ----------------
        # Add current element to subset
        arr.append(nums[idx])

        # Move to next index
        self.subsetsRecursive(idx + 1, nums, arr)

        # ---------------- BACKTRACK ----------------
        # Remove the element we just added
        # so we can explore the "exclude" path
        arr.pop()

        # ---------------- CHOICE 2: EXCLUDE nums[idx] ----------------
        # Do NOT include nums[idx], just move forward
        self.subsetsRecursive(idx + 1, nums, arr)