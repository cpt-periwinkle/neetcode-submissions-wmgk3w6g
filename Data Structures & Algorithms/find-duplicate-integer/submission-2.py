class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ---- Phase 1: Detect cycle (Floyd's Tortoise & Hare) ----

        # Treat array as a linked list:
        # index → nums[index]
        # Because values are in [1, n], a cycle must exist (pigeonhole principle)

        slow = 0
        fast = 0

        # Move slow by 1 step, fast by 2 steps
        # They will meet inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # ---- Phase 2: Find cycle entry (duplicate number) ----

        slow2 = 0

        # ----------- MATH EXPLANATION -----------
        # Let:
        # μ = distance from start to cycle entry
        # λ = length of the cycle
        #
        # When slow and fast meet:
        #   slow has traveled t steps
        #   fast has traveled 2t steps
        #
        # Since fast laps slow inside the cycle:
        #   2t = t + k·λ
        # → t = k·λ   (k is some integer)
        #
        # So slow is k full cycles inside the loop
        #
        # Now:
        # - slow is at meeting point (k·λ steps from start)
        # - slow2 starts from 0 (start of list)
        #
        # Move both one step at a time:
        # After μ steps:
        #   slow has moved μ steps further → reaches cycle entry
        #   slow2 has moved μ steps from start → reaches cycle entry
        #
        # → They meet exactly at the cycle entry (duplicate number)
        # ---------------------------------------

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow  # cycle entry = duplicate