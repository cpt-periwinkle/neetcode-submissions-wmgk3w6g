class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.stack = []
        self.res = []
        self.n = n
        self.backtrack(0, 0)
        return self.res
    
    def backtrack(self, openN, closedN):
        if openN == closedN == self.n:
            self.res.append("".join(self.stack))
            return
        if openN < self.n:
            self.stack.append("(")
            self.backtrack(openN + 1, closedN)
            self.stack.pop()
        if closedN < openN:
            self.stack.append(")")
            self.backtrack(openN, closedN + 1)
            self.stack.pop()