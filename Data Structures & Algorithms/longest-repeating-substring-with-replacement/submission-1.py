class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        right = 0
        res = 0
        max_freq = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            while ((right - left + 1) - max_freq > k):
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
        