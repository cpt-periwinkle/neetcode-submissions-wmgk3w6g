class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> numStack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (!tokens[i].equals("*") && !tokens[i].equals("/") && !tokens[i].equals("-")
                    && !tokens[i].equals("+"))   {
                numStack.push(Integer.parseInt(tokens[i]));
                continue;
            }
            int val1 = numStack.pop();
            int val2 = numStack.pop();
            if (tokens[i].equals("*"))   {
                numStack.push((val2 * val1));
            } else if (tokens[i].equals("/"))    {
                numStack.push((val2 / val1));
            } else if (tokens[i].equals("-"))    {
                numStack.push((val2 - val1));
            } else  {
                numStack.push((val2 + val1));
            }
        }
        return numStack.pop();
    }
}
