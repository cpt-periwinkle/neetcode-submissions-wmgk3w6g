class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # hashmap to store frequency of characters in current window
        res = 0         # stores the maximum valid window length

        left = 0        # left pointer of sliding window
        maxf = 0        # frequency of the most common character in current window

        for right in range(len(s)):
            # Add current character to hashmap (increment frequency)
            count[s[right]] = 1 + count.get(s[right], 0)

            # Track the maximum frequency character seen so far in the window
            maxf = max(maxf, count[s[right]])

            # IMPORTANT NOTE ABOUT maxf:
            # maxf can become "stale" (i.e., not reflect the true max in the current window)
            # but this does NOT affect correctness.

            # Why?
            # - maxf is only used to check if the window is valid
            # - If maxf is overestimated, we might allow a slightly larger window
            # - This only delays shrinking, but does NOT cause incorrect results
            # - Since we are maximizing window size, this is safe

            # Intuition:
            # (window size - maxf) = number of replacements needed
            # If this exceeds k → window becomes invalid

            # Shrink window if more than k replacements are needed
            while (right - left + 1) - maxf > k:
                # Remove the leftmost character from window
                count[s[left]] -= 1
                left += 1

            # Update result with the maximum valid window size
            res = max(res, right - left + 1)

        return res