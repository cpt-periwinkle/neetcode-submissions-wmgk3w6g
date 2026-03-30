class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> hm1 = new HashMap<>();
        HashMap<Character, Integer> hm2 = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            hm1.put(s.charAt(i), hm1.getOrDefault(s.charAt(i), 0) + 1);
            hm2.put(t.charAt(i), hm2.getOrDefault(t.charAt(i), 0) + 1);
        }
        return hm1.equals(hm2);
    }
}
