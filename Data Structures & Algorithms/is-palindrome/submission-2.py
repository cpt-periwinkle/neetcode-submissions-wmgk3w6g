class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        i = 0                  # left pointer
        j = length - 1         # right pointer

        # Use two pointers moving toward each other
        while i < j:

            # Skip non-alphanumeric characters from the left
            while i < j and not s[i].isalnum():
                i += 1

            # Skip non-alphanumeric characters from the right
            while i < j and not s[j].isalnum():
                j -= 1

            # Compare characters ignoring case
            if s[i].lower() != s[j].lower():
                return False

            # Move both pointers inward
            i += 1
            j -= 1

        # If all characters matched, it's a palindrome
        return True