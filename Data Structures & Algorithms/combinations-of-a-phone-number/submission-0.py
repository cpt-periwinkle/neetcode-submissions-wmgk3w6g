class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Store input and result
        self.digits = digits
        self.res = []

        # Mapping of digits to letters (like a phone keypad)
        self.digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Only start DFS if input is non-empty
        # (empty input should return [])
        if self.digits:
            self.dfs(0, "")

        return self.res

    def dfs(self, i, currStr):
        # Base case:
        # If we've chosen one character for each digit,
        # we've built a complete combination
        if len(currStr) == len(self.digits):
            self.res.append(currStr)
            return

        # Recursive case:
        # Look at the current digit and try all its possible letters
        for ch in self.digits_to_char[self.digits[i]]:
            # Choose one letter and move to the next digit
            # (build the string step by step)
            self.dfs(i + 1, currStr + ch)