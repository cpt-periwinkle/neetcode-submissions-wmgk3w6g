class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> stack = new Stack<>();
        int maxArea = 0;
        for (int i = 0; i < heights.length; i++)    {
            int start = i;
            while (!stack.isEmpty() && stack.peek()[1] > heights[i])   {
                int[] tempArr = stack.pop();
                maxArea = Math.max(maxArea, tempArr[1] * (i - tempArr[0]));
                start = tempArr[0];
            }
            stack.push(new int[]{start, heights[i]});
        }
        while (!stack.isEmpty())    {
            int[] tempArr = stack.pop();
            maxArea = Math.max(maxArea, tempArr[1] * (heights.length - tempArr[0]));
        }
        return maxArea;
    }
}
