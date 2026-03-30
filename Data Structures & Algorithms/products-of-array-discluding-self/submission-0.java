class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefixArray = new int[nums.length];
        int[] suffixArray = new int[nums.length];
        int prodVal = 1;
        prefixArray[0] = 1;
        suffixArray[nums.length - 1] = 1;
        for (int i = 1; i < nums.length; i++)   {
            prefixArray[i] = prefixArray[i-1] * nums[i-1];
        }
        for (int j = nums.length - 2; j >= 0; j--)  {
            suffixArray[j] = suffixArray[j+1] * nums[j+1];
        }
        for (int k = 0; k < nums.length; k++)   {
            nums[k] = prefixArray[k] * suffixArray[k];
        }
        return nums;
    }
}  
