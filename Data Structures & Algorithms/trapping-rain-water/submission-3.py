class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0     # sum of areas to get rainwater
        left = 0    # left pointer
        right = len(height) - 1     # right pointer
        
        max_left = height[left]     # local maximum at that point of time (left)
        max_right = height[right]   # local maximum at that point of time (right)

        while (left < right):
            if (max_left < max_right):          # these become the bottlenecks for the current element. As long as one max is bigger at that point of time, water can be filled
                left += 1                       # movement according to who has the current smaller element
                max_left = max(max_left, height[left])  # takes the max between the two so as to not have negative values in solution
                ans += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                ans += max_right - height[right]
        return ans
