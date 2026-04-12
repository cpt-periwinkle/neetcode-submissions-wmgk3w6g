class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # Iterate over every possible center
        for i in range(len(s)):

            # 1. Odd length palindromes (center at i)
            l, r = i, i

            # Expand outward while valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1   # every expansion = one palindrome
                l -= 1       # move left pointer outward
                r += 1       # move right pointer outward

            # 2. Even length palindromes (center between i and i+1)
            l, r = i, i + 1

            # Expand outward while valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1   # count this palindrome
                l -= 1
                r += 1

        return count