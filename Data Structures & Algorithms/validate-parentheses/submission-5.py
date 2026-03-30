class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(",
                    "]" : "[",
                    "}" : "{"}  # creates a mapping to check through instead of writing conditions repititively
        for char in s:
            if char in mapping:         # checks for ending bracket
                if not stack or stack[-1] != mapping[char]:        # checks if empty or if last element is equal to the associated start bracket   
                    return False    # returns false if not present
                stack.pop()         # if conditions fail, pops the last element
            else:
                stack.append(char)  # adds if not in the mapping
        return not stack            # returns True only if the stack is empty