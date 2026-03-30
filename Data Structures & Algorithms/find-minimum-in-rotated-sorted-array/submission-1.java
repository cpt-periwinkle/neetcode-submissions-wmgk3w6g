class Solution {
    public int findMin(int[] nums) {
        return findRecursive(nums, 0, nums.length - 1);
    }

    private static int findRecursive(int[] nums, int lb, int ub)   {
        if (lb == ub) {
            return nums[lb];
        }
        int mid = lb + (ub - lb) / 2;
        if (nums[mid] < nums[ub])    {
            return findRecursive(nums, lb, mid);
        } else {
            return findRecursive(nums, mid + 1, ub);
        }
    }
}
