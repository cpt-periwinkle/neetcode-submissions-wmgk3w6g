class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()

        left = 0
        max_length = 0
        
        for right in range(len(s)):     # go through all elements
            while s[right] in sub_set:  # check if the value is in existing hash set. Moves left pointer until the reappeared is removed
                sub_set.remove(s[left])
                left += 1
            sub_set.add(s[right])       # adds the next right element, as it is unique since the duplicates are removed with the moving left pointer
            max_length = max(max_length, (right - left + 1))    # keeps only the max length

        return max_length