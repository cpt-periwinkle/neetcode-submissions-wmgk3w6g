class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []  # this problem requires a stack for test cases like tokens=["2","3","4","+","*"], where the operations may happen later.

        val = 0
        
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                val = b + a
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                val = b - a
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                val = b * a
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                val = int(b / a)
            else:
                val = int(token)
            stack.append(val)

        return stack.pop()
        
        

