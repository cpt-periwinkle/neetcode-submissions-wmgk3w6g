class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        front = 0
        back = len(heights) - 1
        while (front < back):
            curr_height = min(heights[front], heights[back])
            dist = back - front
            curr_area = curr_height * dist
            max_area = max(max_area, curr_area)
            if (heights[front] < heights[back]):    #Reason for this is because area is limited by the height. It will keep the max height, and if the other pointer has a larger height, it shifts, meaning that we can ignore the smaller one
                front += 1
            else:
                back -= 1
        return max_area
        