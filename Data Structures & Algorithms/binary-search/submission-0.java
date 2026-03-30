class Solution {
    public int search(int[] nums, int target) {
        int lb = 0, ub = nums.length - 1;
        return searchRecursive(lb, ub, nums, target);
    }

    private static int searchRecursive(int lb, int ub, int[] nums, int target)  {
        while (true)    {
            if (lb > ub)   {
                return -1;
            }
            int mid = lb + (ub-lb)/2;
            if (nums[mid] == target)    {
                return mid;
            } else if (nums[mid] < target)  {
                return searchRecursive(mid + 1, ub, nums, target);
            } else  {
                return searchRecursive(lb, mid - 1, nums, target);
            }
        }
    }
}
