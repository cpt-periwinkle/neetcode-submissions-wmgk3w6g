class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [-1] * n          # previous smaller index
        nse = [n] * n           # next smaller index
        stack = []

        # Previous Smaller Element
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]

            stack.append(i)

        # clear stack for next pass
        stack = []

        # Next Smaller Element
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # compute max area
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area