class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> solnList = new ArrayList<>();
        if (nums == null || nums.length < 3) {
            return solnList;
        }
        for (int i = 0; i < nums.length; i++)   {
            if (i > 0 && nums[i] == nums[i-1])  {
                continue;
            }
            int j = i + 1, k = nums.length - 1;
            while (j < k)   {
                int sum = nums[j] + nums[k] + nums[i];
                if (sum == 0) {
                    solnList.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j-1])   {
                        j++;
                    }
                } else if (sum > 0 )    {
                    k--;
                } else   {
                    j++;
                }                
            }
        }
        return solnList;
    }
}
