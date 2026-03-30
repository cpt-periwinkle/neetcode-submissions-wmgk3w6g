class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If s is smaller than t, it's impossible to have a valid window
        if len(s) < len(t):
            return ""

        t_freq = {}     # frequency map of characters we need
        window = {}     # frequency map of current sliding window

        # Build frequency map for t
        for ch in t:
            t_freq[ch] = 1 + t_freq.get(ch, 0)
 
        have = 0                        # number of characters that currently meet required frequency
        need = len(t_freq)              # number of unique characters required

        res = [-1, -1]                  # stores best window indices
        min_length = float("inf")       # length of smallest valid window found
        left = 0                        # left pointer of sliding window

        # Expand the window using right pointer
        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)

            # If this character now satisfies the required frequency, increment 'have'
            if (ch in t_freq) and (window[ch] == t_freq[ch]):
                have += 1

            # If all required characters are satisfied, try shrinking from the left
            while (have == need):
                # Update result if this window is smaller than previous best
                if ((right - left + 1) < min_length):
                    res = [left, right]
                    min_length = right - left + 1

                # Remove the left character from the window
                window[s[left]] -= 1

                # If removing breaks a required frequency, reduce 'have'
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]:
                    have -= 1

                # Move left pointer to shrink the window
                left += 1

        # Extract result substring using stored indices
        start, end = res
        if min_length != float("inf"):
            return s[start : end + 1]
        else:
            return ""