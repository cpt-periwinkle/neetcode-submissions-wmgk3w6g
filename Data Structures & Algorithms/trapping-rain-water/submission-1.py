class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0
        left = 0
        right = len(height) - 1
        
        max_left = height[left]
        max_right = height[right]

        while (left < right):
            if (max_left < max_right):
                left += 1
                max_left = max(max_left, height[left])
                val = max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                val = max_right - height[right]
            if (val > 0):
                ans += val
        return ans
