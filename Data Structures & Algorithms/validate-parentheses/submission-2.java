class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        if (len % 2 != 0)    {
            return false;
        }
        Stack<Character> values = new Stack<>();
        for (int i = 0; i < len; i++)    {
            char ch = s.charAt(i);
            if (ch == '{' || ch == '[' || ch == '(')    {
                values.push(ch);
            } else {
                if (values.isEmpty())   {
                    return false;
                }
                int top = values.pop();
                if ((ch == ')' && top != '(') || (ch == ']' && top != '[') ||
                        (ch == '}' && top != '{'))    {
                    return false;
                }
            }
        }
        return values.isEmpty();    
    }
}
