class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res stores the longest palindrome found so far
        # resLen stores its length
        res = ""
        resLen = 0

        # We treat every index as a potential "center" of a palindrome
        for i in range(len(s)):

            # --- Case 1: Odd length palindrome ---
            # Center is exactly at index i (like "aba")
            l, r = i, i

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If this palindrome is longer, update result
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                # Expand window outward
                l -= 1
                r += 1

            # --- Case 2: Even length palindrome ---
            # Center is between i and i+1 (like "abba")
            l, r = i, i + 1

            # Expand outward while characters match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update result if longer palindrome is found
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                # Expand window outward
                l -= 1
                r += 1

        # Return the longest palindrome substring found
        return res