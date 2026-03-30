class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> checkSet =  new HashSet<>();
        for (int num : nums)    {
            checkSet.add(num);
        }
        if (checkSet.size() != nums.length)
            return true;
        return false;
    }
}