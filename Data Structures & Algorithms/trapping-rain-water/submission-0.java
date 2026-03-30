class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }
        
        int i = 0, j = height.length - 1, lb = height[i], rb = height[j];
        int totalArea = 0;
        while (i < j)    {
            if (lb < rb)    {
                i++;
                lb = Math.max(lb, height[i]);
                totalArea += lb - height[i];
            } else {
                j--;
                rb = Math.max(rb, height[j]);
                totalArea += rb - height[j];
            }
        }
        return totalArea;
    }
}