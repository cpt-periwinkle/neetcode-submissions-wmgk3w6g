class Solution {
    public boolean isPalindrome(String s) {
        if (s.equals(""))  {
            return false;
        }
        s = s.toLowerCase();
        int i = 0, j = s.length() - 1;
        while (i < j)   {
            char fp = s.charAt(i);
            char lp = s.charAt(j);
            if (!Character.isLetterOrDigit(fp))  {
                i++;
                continue;
            }
            if (!Character.isLetterOrDigit(lp))  {
                j--;
                continue;
            }
            if (fp != lp)   {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
