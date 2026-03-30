class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        sub_set = set()

        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1

            sub_set.add(s[right])
            length = right - left + 1
            max_length = max(max_length, length)

        return max_length