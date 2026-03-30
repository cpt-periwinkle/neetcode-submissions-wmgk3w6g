class Solution {
    public int maxArea(int[] heights) {
        int i = 0, j = heights.length - 1, maxArea = 0;
        while (i < j)   {
            int distance = j - i;
            int area = distance * Math.min(heights[i], heights[j]);
            maxArea = Math.max(area, maxArea);
            if (heights[i] >= heights[j])    {
                j--;
            }
            if (heights[i] < heights[j])    {
                i++;
            }
        }
        return maxArea;
    }
}
