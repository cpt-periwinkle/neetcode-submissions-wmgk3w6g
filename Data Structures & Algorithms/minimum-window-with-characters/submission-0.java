class Solution {
    public String minWindow(String s, String t) {
        if (t.equals("") && t.length() > s.length())    {
            return "";
        }

        Map<Character, Integer> tMap = new HashMap<>();
        Map<Character, Integer> sMap = new HashMap<>();
        for (int i = 0; i < t.length(); i++)    {
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
        }

        int have = 0, need = tMap.size();
        int[] soln = {-1, -1};
        int solnLen = Integer.MAX_VALUE;
        int l = 0;

        for (int r = 0; r < s.length(); r++)    {
            char curr = s.charAt(r);
            sMap.put(curr, sMap.getOrDefault(curr, 0) + 1);
            if (tMap.containsKey(curr) && sMap.get(curr).equals(tMap.get(curr))) {
                have++;
            }
            while (have == need)    {
                if ((r - l + 1) < solnLen)  {
                    solnLen = r - l + 1;
                    soln[0] = l;
                    soln[1] = r;
                }
                char lChar = s.charAt(l);
                sMap.put(lChar, sMap.get(lChar) - 1);
                if (tMap.containsKey(lChar) && sMap.get(lChar) < tMap.get(lChar)) {
                    have--;
                }
                l++;
            }
        }
        return solnLen == Integer.MAX_VALUE ? "" : s.substring(soln[0], soln[1] + 1);
    }
}
