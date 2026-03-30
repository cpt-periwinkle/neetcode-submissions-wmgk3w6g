class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String item:strs)   {
            sb.append(item.length()).append("?").append(item);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        int i = 0;
        while (i < str.length())    {
            int delimIndex = str.indexOf("?", i);
            if (delimIndex == -1) break;
            int length = Integer.parseInt(str.substring(i, delimIndex));
            strs.add(str.substring(delimIndex + 1, delimIndex + length + 1));
            i = delimIndex + length + 1;
        }
        return strs;
    }
}
