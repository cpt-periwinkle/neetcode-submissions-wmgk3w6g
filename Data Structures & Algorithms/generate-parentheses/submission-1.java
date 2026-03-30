class Solution {
    private void recursiveGenerate( List<String> res, Stack<Character> stack,
            int open, int close, int n)    {
        if (open == n && close == n) {
            StringBuilder sb = new StringBuilder();
            for (char ch : stack)   {
                sb.append(ch);
            }
            res.add(sb.toString());
            return;
        }
        if (open < n)   {
            stack.push('(');
            recursiveGenerate(res, stack, open + 1, close, n);
            stack.pop();
        }
        if (close < open) {
            stack.push(')');
            recursiveGenerate(res, stack, open, close + 1, n);
            stack.pop();
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        recursiveGenerate(res, stack, 0, 0, n);
        return res;
    }
}
