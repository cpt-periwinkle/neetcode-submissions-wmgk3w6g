class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int maxf = 0;
        int soln  = 0;
        Map<Character, Integer> freqCount = new HashMap<>();
        for (int r = 0; r < s.length(); r++)    {
            char temp = s.charAt(r);
            freqCount.put(temp, freqCount.getOrDefault(temp, 0) + 1);
            maxf = Math.max(maxf, freqCount.get(temp));
            while (((r - l + 1) - maxf) > k)    {
                char temp2 = s.charAt(l);
                freqCount.put(temp2, freqCount.get(temp2) - 1);
                l++;
            }
            soln = Math.max(soln, r - l + 1);
        }
        return soln;
    }
}
