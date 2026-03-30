class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26            # Get O(1) space through an array of size 26
        left = 0                    # left pointer
        right = 0                   # right pointer
        res = 0                     # answer -> the length of the string with one distinct letter
        max_freq = 0                # max frequency of the character array at that time

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')              # get the current 
            count[idx] += 1                             # counting for the letter at that point
            max_freq = max(max_freq, count[idx])        # max frequency of char at that time

            while ((right - left + 1) - max_freq > k):      # our window size (r - l + 1) minus the max frequency would give us the number of changes that could be made. If this number is over the changes possible (k), it is invalid, so we would shorten it
                left_idx = ord(s[left]) - ord('A')          # we reduce the window size so it becomes valid again, requiring a reduce of the count of the left pointer element (the one we're taking in to reduce the window size)
                count[left_idx] -= 1
                left += 1
            
            res = max(res, right - left + 1)            # The largest possible window size would be the correct answer

        return res
        