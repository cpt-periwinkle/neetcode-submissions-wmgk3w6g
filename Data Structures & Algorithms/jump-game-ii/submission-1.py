class Solution:
    def jump(self, nums: List[int]) -> int:
        # We treat this like BFS on an implicit graph:
        # - Each index is a node
        # - From index i, you can go to [i+1 ... i+nums[i]]
        # Goal: reach last index in minimum jumps (levels)

        l, r = 0, 0   # Current "window" (level) of indices we can reach
        step = 0      # Number of jumps (levels processed)

        while r < len(nums) - 1:
            # We will compute the next window (next level)
            # by finding the farthest we can reach from current window
            farthest = 0

            # Explore all nodes in current level [l, r]
            for i in range(l, r + 1):
                # From index i, we can reach up to i + nums[i]
                # Take the maximum across all options
                farthest = max(farthest, i + nums[i])

            # Move to next level:
            # new window starts right after current window
            l = r + 1
            r = farthest

            # We just used one jump to expand to next level
            step += 1

        return step