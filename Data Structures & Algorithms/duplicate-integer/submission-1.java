class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for (int num : nums)    {
            hs.add(num);
        }
        return hs.size() != nums.length;
    }
}
