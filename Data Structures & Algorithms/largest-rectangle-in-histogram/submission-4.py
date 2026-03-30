class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = [-1] * n          # previous smaller index
        nse = [n] * n           # next smaller index
        stack = []

        # REMEMBER -> WE ARE USING INDICES IN PSE AND NSE. WE USE THOSE TO COMPARE IN OUR CONDITIONS TOO!

        # Previous Smaller Element -> We go in order. The while loop appends numbers until an index with a smaller number is reached and then pops the other greater number indices until it meets a smaller number index. Then it goes to the next element
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:   # this condition is checking if the stack exists, which has montonically increasing elements. If it encounters something smaller, it pops the elements till it finds the smallest
                stack.pop()

            if stack:           # whatever makes the while condition false with the stack not being empty is the index of the smallest element for i
                pse[i] = stack[-1]

            stack.append(i)     # sticks it in the stack for checking

        # clear stack for next pass
        stack = []

        # Next Smaller Element -> We go in reverse. The concept is the same as the previous, except the reverse allows us to get the next smallest element instead.
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # compute max area -> Now that we have nse and pse, we can basically start multiplying and finding our max_area (length * width)
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1     # The width of the rectangle would be based on how far we can extend that element, so by saving nse and pse at i, we can subtract the two and get the width and multiply it with the corresponding i height
            area = heights[i] * width
            max_area = max(max_area, area)  # we only want the max area, so this works out

        return max_area