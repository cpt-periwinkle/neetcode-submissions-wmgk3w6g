class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] temp = strs[i].toCharArray();
            Arrays.sort(temp);
            String sortStr = new String(temp);
            map.putIfAbsent(sortStr, new ArrayList<>());
            map.get(sortStr).add(strs[i]);
        }
        return new ArrayList<>(map.values());
    }
}
