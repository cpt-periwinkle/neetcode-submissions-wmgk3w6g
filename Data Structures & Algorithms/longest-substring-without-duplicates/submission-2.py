class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current window
        sub_set = set()

        # Left pointer of the sliding window
        left = 0

        # Tracks the maximum length of valid substring
        max_length = 0
        
        # Expand the window using 'right' pointer
        for right in range(len(s)):

            # If duplicate character is found,
            # shrink the window from the left until it's removed
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1

            # Add current character (now guaranteed unique in window)
            sub_set.add(s[right])

            # Update maximum length of substring
            # Window size = right - left + 1
            max_length = max(max_length, right - left + 1)

        return max_length