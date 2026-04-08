class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack stores the current parentheses string being built
        self.stack = []

        # res stores all valid combinations
        self.res = []

        # total number of pairs we need to generate
        self.n = n

        # start backtracking with 0 open and 0 closed brackets
        self.backtrack(0, 0)
        return self.res
    
    def backtrack(self, openN, closedN):
        # Base case:
        # If we have used all opening and closing brackets,
        # we formed a valid parentheses string
        if openN == closedN == self.n:
            self.res.append("".join(self.stack))
            return

        # ---- CHOICE 1: Add "(" ----
        # We can always add "(" as long as we haven't used all n of them
        if openN < self.n:
            self.stack.append("(")
            self.backtrack(openN + 1, closedN)
            self.stack.pop()  # backtrack

        # ---- CHOICE 2: Add ")" ----
        # We can only add ")" if it won't make the string invalid
        # i.e., we must have more "(" than ")" so far
        if closedN < openN:
            self.stack.append(")")
            self.backtrack(openN, closedN + 1)
            self.stack.pop()  # backtrack