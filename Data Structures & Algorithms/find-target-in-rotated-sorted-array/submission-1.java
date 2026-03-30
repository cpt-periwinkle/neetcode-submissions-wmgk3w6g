class Solution {
    public int search(int[] nums, int target) {
        return searchRecursive(nums, target, 0, nums.length - 1);
    }

    private int searchRecursive(int[] nums, int target, int lb, int ub) {
        if (lb > ub) {
            return -1;
        }
        
        int mid = lb + (ub - lb) / 2;
        
        if (nums[mid] == target) {
            return mid;
        }
        
        if (nums[lb] <= nums[mid]) {
            if (nums[lb] <= target && target < nums[mid]) {
                return searchRecursive(nums, target, lb, mid - 1);
            } else {
                return searchRecursive(nums, target, mid + 1, ub);
            }
        } 
        else {
            if (nums[mid] < target && target <= nums[ub]) {
                return searchRecursive(nums, target, mid + 1, ub);
            } else {
                return searchRecursive(nums, target, lb, mid - 1);
            }
        }
    }
}