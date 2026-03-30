class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
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
        
        

