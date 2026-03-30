class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack to keep track of opening brackets

        # Mapping of closing → corresponding opening brackets
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Traverse each character in the string
        for char in s:
            if char in mapping:
                # If it's a closing bracket:
                # 1. Stack should not be empty
                # 2. Top of stack must match the corresponding opening bracket
                if not stack or stack[-1] != mapping[char]:
                    return False  # Invalid if mismatch or no opening bracket available

                # Valid match → pop the opening bracket
                stack.pop()
            else:
                # If it's an opening bracket, push onto stack
                stack.append(char)

        # At the end, stack should be empty for a valid string
        return not stack